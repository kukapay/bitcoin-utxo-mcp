# Bitcoin UTXO MCP

An MCP server that tracks Bitcoin's Unspent Transaction Outputs (UTXO) and block statistics, giving AI agents direct access to essential on-chain data.

![GitHub License](https://img.shields.io/github/license/kukapay/bitcoin-utxo-analytics-mcp) 
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## Features

- **Tools**:
  - `get_utxo`: Retrieves UTXO details for a given Bitcoin address, including the number of UTXOs, total value in BTC, and transaction details.
  - `get_block_stats`: Fetches transaction statistics for a specific Bitcoin block, including block hash, transaction count, total value, and block time.
- **Prompt**:
  - `analyze_bitcoin_flow`: A reusable prompt template for LLMs to analyze Bitcoin funds flow, network health, and potential market impacts based on UTXO and block data.

## Installation

### Prerequisites

- **Python**: Version 3.10 or higher
- **uv**: A fast and modern Python package manager ([installation instructions](https://docs.astral.sh/uv/))

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kukapay/bitcoin-utxo-mcp.git
   cd bitcoin-utxo-mcp
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Install to Claude Desktop**:

    Install the server as a Claude Desktop application:
    ```bash
    uv run mcp install main.py --name "Bitcoin UTXO"
    ```

    Configuration file as a reference:

    ```json
    {
       "mcpServers": {
           "Bitcoin UTXO": {
               "command": "uv",
               "args": [ "--directory", "/path/to/bitcoin-utxo-mcp", "run", "main.py" ]
           }
       }
    }
    ```
    Replace `/path/to/bitcoin-utxo-mcp` with your actual installation path.
 
   ```

## Usage

### Available Tools and Prompts

- **Tools**:
  - `get_utxo(address: str)`: Returns UTXO details for a Bitcoin address, e.g., "Address 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa: 50 UTXOs, Total Value: 50.00000000 BTC, UTXO Details: ...".
  - `get_block_stats(block_height: int)`: Returns block statistics, e.g., "Block Height: 0, Block Hash: 000000000019d668..., Transactions: 1, Total Value: 50.00000000 BTC, Block Time: 1231006505".
- **Prompt**:
  - `analyze_bitcoin_flow()`: Generates a prompt for LLMs to analyze UTXO and block data, e.g., "Analyze the provided Bitcoin UTXO and block data: What do the UTXO distributions indicate about funds flow? ...".

### Example Interaction

Below are examples of natural language prompts you might use in an MCP-compatible client (e.g., Claude Desktop) and the corresponding outputs from the server, based on hypothetical Blockchain.com API responses.

1. **Get UTXO for a Bitcoin Address**:
   - **Prompt**: "Show me the UTXO details for the Bitcoin genesis address."
   - **Command**: `get_utxo("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")`
   - **Output**:
     ```
     Address 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa:
     50 UTXOs
     Total Value: 50.00000000 BTC
     UTXO Details:
     - TXID: 4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b, Value: 50.00000000 BTC, Confirmations: 800000
     ```

2. **Get Block Statistics**:
   - **Prompt**: "What's the transaction data for the Bitcoin genesis block?"
   - **Command**: `get_block_stats(0)`
   - **Output**:
     ```
     Block Height: 0
     Block Hash: 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
     Transactions: 1
     Total Value: 50.00000000 BTC
     Block Time: 1231006505
     ```

3. **Analyze Bitcoin Flow**:
   - **Prompt**: "Analyze Bitcoin funds flow and network health."
   - **Command**: `analyze_bitcoin_flow()`
   - **Output** (prompt sent to LLM for analysis):
     ```
     Analyze the provided Bitcoin UTXO and block data:
     - What do the UTXO distributions indicate about funds flow?
     - How does the block statistics reflect network health (e.g., transaction volume, congestion)?
     - Provide insights on potential market impacts or trends.
     ```
     - **LLM Response** (example, depends on the LLM):
       ```
       The UTXO distribution for the queried address shows a significant number of unspent outputs, indicating long-term holding behavior, possibly by an early adopter. The genesis block's single transaction with 50 BTC reflects the initial reward structure. Current block statistics suggest stable network health with consistent transaction volumes. High UTXO consolidation may signal preparation for large transfers, potentially impacting market liquidity if moved. Historically, such patterns precede price volatility.
       ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

