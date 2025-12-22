# Φ-Chain Wallet and Proof-of-Coherence (PoC) Mining Application

## Overview

This repository contains the source code for the official Φ-Chain Wallet and Proof-of-Coherence (PoC) Mining Application. Φ-Chain is a blockchain operating on universal mathematical law, where every parameter derives from the Golden Ratio and the Fibonacci sequence.

## Key Features

### Wallet Functionality
*   **Secure Wallet Creation (New!):** Easily generate a new, non-custodial wallet with a unique 12-word mnemonic phrase and private key.
*   **Wallet Connection:** Connect seamlessly with existing wallets such as MetaMask, Phantom, and WalletConnect.
*   **Asset Management:** View your Φ token balance, staked sΦ tokens, and transaction history.

### Mining Functionality
*   **PoC Mining:** Interface for starting and monitoring the Proof-of-Coherence mining process.

## Getting Started

### Prerequisites

*   A modern web browser (Chrome, Firefox, Edge).
*   For connecting existing wallets, the respective browser extension (e.g., MetaMask, Phantom) is required.

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/badreddine023/phi-chain.git
    cd phi-chain
    ```
2.  **Open the application:**
    Simply open `index.html` or `wallet.html` in your web browser.

## Development

The wallet functionality is primarily handled by the following files:
*   `wallet.html`: The main wallet interface and UI logic.
*   `js/web3-connector.js`: Contains the logic for connecting to external wallets and the newly added `createNewWallet()` function using `ethers.js`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
