# Ethereum Price & Gas Bot 🤖

A Twitter bot that automatically tweets Ethereum price updates and gas prices every 15 minutes. The bot provides real-time information about ETH price and gas fees in an easy-to-read format.

## 🌟 Features

- 🔄 Updates every 15 minutes
- 💰 Real-time ETH price updates from CoinGecko
- ⛽ Current gas prices from Etherscan
- 🔁 Automatic retry mechanism on failures
- 📝 Comprehensive error logging
- 🎨 Clean, emoji-formatted output
- 🏷️ Relevant hashtags

## 📊 Example Tweet Format

```
🔄 Ethereum Update (2024-12-08 01:05:56 UTC)

💰 ETH Price: $4,011.51
⛽ Gas Prices (Gwei):
   Safe Low: 12.438175555
   Standard: 12.442774287
   Fast: 12.57631155

#Ethereum #ETH #GasPrice
```

## 🔧 Prerequisites

- Python 3.8 or higher
- Twitter Developer Account with Elevated access
- Etherscan API Key

## 📁 Project Structure

```
eth-price-bot/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── src/
    ├── __init__.py
    ├── config.py
    ├── api/
    │   ├── __init__.py
    │   ├── etherscan.py
    │   ├── coingecko.py
    │   └── twitter.py
    ├── utils/
    │   ├── __init__.py
    │   └── formatter.py
    └── bot.py
```

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/eth-price-bot.git
cd eth-price-bot
```

2. **Create and activate virtual environment**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install required packages**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

```bash
cp .env.example .env
```

5. **Configure your `.env` file with your API credentials**

```plaintext
# Twitter API Credentials
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET=your_api_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

# Etherscan API
ETHERSCAN_API_KEY=your_etherscan_api_key
```

## 🎮 Usage

1. **Run the bot**

```bash
python -m src.bot
```

2. **For production deployment**

- Use a process manager like PM2:

```bash
pm2 start src/bot.py --name eth-price-bot
```

- Or create a system service (recommended for Linux servers)

## 📝 Logging

The bot creates a log file `eth_bot.log` with detailed information about its operation, including:

- Successful tweets
- Error messages
- Retry attempts

## 🛠️ Configuration

You can modify the following settings in `src/config.py`:

- Update interval (default: 15 minutes)
- Retry interval (default: 5 minutes)
- API endpoints

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes

```bash
git commit -m 'Add some AmazingFeature'
```

4. Push to the branch

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

## 🐛 Bug Reports

If you discover any bugs, please create an issue in the GitHub repository including:

- Expected behavior
- Actual behavior
- Steps to reproduce
- Any relevant error messages

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CoinGecko API](https://www.coingecko.com/en/api) for ETH price data
- [Etherscan API](https://etherscan.io/apis) for gas prices
- [Twitter API](https://developer.twitter.com/en) for tweet functionality

## 📫 Contact

Twitter - @wittymw (https://twitter.com/wittymw)

Project Link: [https://github.com/wittymw/eth-price-bot-x]

## ⚠️ Disclaimer

This bot is for informational purposes only. Cryptocurrency prices and gas fees can be volatile. Always do your own research before making any financial decisions.
