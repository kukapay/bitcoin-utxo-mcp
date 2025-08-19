import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Bitcoin UTXO Analytics",
    dependencies=["httpx"]
)


@mcp.tool()
async def get_utxo(address: str) -> str:
    """Get UTXO for a Bitcoin address.
    
    Args:
        address (str): Bitcoin address (base58 or bech32 format)
    
    Returns:
        A string containing:
        - Address
        - Number of UTXOs
        - Total value in BTC
        - List of UTXO details (txid, value, confirmations)
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"https://blockchain.info/unspent?active={address}")
            response.raise_for_status()
            data = response.json()
            utxos = data.get("unspent_outputs", [])
            total_value = sum(u['value'] for u in utxos) / 1e8
            utxo_details = "\n".join(
                f"- TXID: {u['tx_hash_big_endian']}, Value: {u['value'] / 1e8:.8f} BTC, Confirmations: {u['confirmations']}"
                for u in utxos
            )
            return (
                f"Address {address}:\n"
                f"{len(utxos)} UTXOs\n"
                f"Total Value: {total_value:.8f} BTC\n"
                f"UTXO Details:\n{utxo_details}"
            )
        except Exception as e:
            return f"Error fetching UTXO: {str(e)}"


@mcp.tool()
async def get_block_stats(block_height: int) -> str:
    """Get transaction statistics for a specific Bitcoin block.
    
    Args:
        block_height (int): The height of the block
    
    Returns:
        A string containing:
        - Block height
        - Block hash
        - Number of transactions
        - Total transaction value in BTC
        - Block time
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"https://blockchain.info/block-height/{block_height}?format=json")
            response.raise_for_status()
            data = response.json()["blocks"][0]
            tx_count = len(data["tx"])
            total_value = sum(tx["out"][0]["value"] for tx in data["tx"] if tx["out"]) / 1e8
            block_time = data["time"]
            return (
                f"Block Height: {block_height}\n"
                f"Block Hash: {data['hash']}\n"
                f"Transactions: {tx_count}\n"
                f"Total Value: {total_value:.8f} BTC\n"
                f"Block Time: {block_time}"
            )
        except Exception as e:
            return f"Error fetching block stats: {str(e)}"


@mcp.prompt()
def analyze_bitcoin_flow() -> str:
    """Prompt to analyze Bitcoin funds flow and network health.
    
    Returns:
        A string prompt for LLM analysis of Bitcoin UTXO and block data, including:
        - Funds flow implications
        - Network health indicators
        - Potential market impacts
    """
    return (
        "Analyze the provided Bitcoin UTXO and block data:\n"
        "- What do the UTXO distributions indicate about funds flow?\n"
        "- How does the block statistics reflect network health (e.g., transaction volume, congestion)?\n"
        "- Provide insights on potential market impacts or trends."
    )


if __name__ == "__main__":
    mcp.run()
