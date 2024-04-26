from web3 import Web3, HTTPProvider
from web3.types import TxParams, Wei


network_api = {
    "ETH":"https://rpc.ankr.com/eth",
    "POLYGON":"https://rpc.ankr.com/polygon",
    "AVAXC":"https://1rpc.io/avax/c",
    "FTM":"https://1rpc.io/ftm",
    "BSC":"https://binance.llamarpc.com",
    "ARBITRUM": "https://arb1.arbitrum.io/rpc",
}

CashVault_ABI = '[{"inputs": [{"internalType": "uint256", "name": "startTime", "type": "uint256"}, {"internalType": "uint256", "name": "period", "type": "uint256"}, {"internalType": "uint256", "name": "_collatCap", "type": "uint256"}, {"internalType": "address", "name": "collatAddress", "type": "address"}, {"internalType": "contract HistoricalPriceConsumerV3_1", "name": "_priceReader", "type": "address"}, {"internalType": "contract AggregatorProxy", "name": "linkAggregator", "type": "address"}, {"internalType": "bytes", "name": "baseSymbol", "type": "bytes"}, {"internalType": "bytes", "name": "quoteSymbol", "type": "bytes"}], "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "uint256", "name": "", "type": "uint256"}], "name": "AdminAction", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": true, "internalType": "address", "name": "spender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "_from", "type": "address"}, {"indexed": true, "internalType": "uint256", "name": "_epoch", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "_amt", "type": "uint256"}, {"indexed": true, "internalType": "address", "name": "_msgSender", "type": "address"}], "name": "Deposit", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "_from", "type": "address"}, {"indexed": true, "internalType": "uint256", "name": "_epoch", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "_strikeX1e6", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "_premium", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "_minSizeOfVault", "type": "uint256"}], "name": "NewEpoch", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "_from", "type": "address"}, {"indexed": true, "internalType": "uint256", "name": "_epoch", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "_amt", "type": "uint256"}, {"indexed": true, "internalType": "address", "name": "_msgSender", "type": "address"}], "name": "QueueWithdraw", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "uint256", "name": "_epoch", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "_strikeX1e6", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "_oracleTime", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "_settlementLoss", "type": "uint256"}], "name": "Settlement", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "_from", "type": "address"}, {"indexed": true, "internalType": "uint256", "name": "_epoch", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "_amt", "type": "uint256"}, {"indexed": true, "internalType": "address", "name": "_msgSender", "type": "address"}], "name": "Withdraw", "type": "event"}, {"inputs": [], "name": "COLLAT", "outputs": [{"internalType": "contract IERC20", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "LINK_AGGREGATOR", "outputs": [{"internalType": "contract AggregatorProxy", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "PERIOD", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "START_TIME", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "priceX1e6", "type": "uint256"}], "name": "_calculateSettlementLoss", "outputs": [{"internalType": "uint256", "name": "settlementLoss", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "aaveV2LendingPool", "outputs": [{"internalType": "contract ILendingPool", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "allowInteractions", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "spender", "type": "address"}], "name": "allowance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "approve", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "collatCap", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "collatLentOut", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "currentEpochAmount", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "currentEpochPremium", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "decimals", "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"}], "name": "decreaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "amt", "type": "uint256"}], "name": "deposit", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "depositIntoLendingPool", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "amt", "type": "uint256"}, {"internalType": "address", "name": "onBehalfOf", "type": "address"}], "name": "depositOnBehalf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "designatedMaker", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "contract IERC20", "name": "token", "type": "address"}], "name": "emergencyWithdraw", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "epoch", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "_epoch", "type": "uint256"}], "name": "epochExpiry", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "expiry", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "feeCollector", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "feePerYearX1e6", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "addedValue", "type": "uint256"}], "name": "increaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256[]", "name": "roundStrikeX1e6", "type": "uint256[]"}, {"internalType": "uint256", "name": "premium", "type": "uint256"}, {"internalType": "uint256", "name": "collatAmt", "type": "uint256"}], "name": "initNewRound", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256[]", "name": "roundStrikeX1e6", "type": "uint256[]"}, {"internalType": "uint256", "name": "premium", "type": "uint256"}, {"internalType": "uint256", "name": "collatAmt", "type": "uint256"}, {"internalType": "uint256", "name": "_signedExpiry", "type": "uint256"}, {"internalType": "address", "name": "_designatedMaker", "type": "address"}, {"internalType": "bytes", "name": "signature", "type": "bytes"}], "name": "initNewRoundSigned", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "amt", "type": "uint256"}], "name": "initWithdraw", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "amt", "type": "uint256"}, {"internalType": "address", "name": "onBehalfOf", "type": "address"}], "name": "initWithdrawOnBehalf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "owner", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "priceReader", "outputs": [{"internalType": "contract HistoricalPriceConsumerV3_1", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "queuedExitEpoch", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "queuedExitLP", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "contract ILendingPoolAddressesProvider", "name": "_ap", "type": "address"}], "name": "setAaveAddressProvider", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "bool", "name": "_flag", "type": "bool"}], "name": "setAllowInteraction", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "arbitraryExpiry", "type": "uint256"}], "name": "setExpiry", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_feeCollector", "type": "address"}], "name": "setFeeCollector", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "_fee", "type": "uint256"}], "name": "setFeePerYearX1e6", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "newMaker", "type": "address"}], "name": "setMaker", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "newDepositCap", "type": "uint256"}], "name": "setMaxCap", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_newOwner", "type": "address"}], "name": "setOwner", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "contract HistoricalPriceConsumerV3_1", "name": "newPriceReader", "type": "address"}], "name": "setPriceReader", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "newValidator", "type": "address"}], "name": "setValidator", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "contract VaultHook", "name": "_newVaultHook", "type": "address"}], "name": "setVaultHook", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "priceX1e6", "type": "uint256"}], "name": "settleStrike_MM", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "settleStrike_chainlink", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "settleStrike_chainlink_fallback", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "signedExpiry", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "strikeX1e6", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "syncBalance", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "totalLPExit", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "totalPendingExit", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transfer", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transferFrom", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "validator", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "valuePerLPX1e18", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "vaultHook", "outputs": [{"internalType": "contract VaultHook", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "withdraw", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "withdrawFromLendingPool", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "onBehalfOf", "type": "address"}], "name": "withdrawOnBehalf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"}]'
ERC20_ABI = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"delegator","type":"address"},{"indexed":true,"internalType":"address","name":"fromDelegate","type":"address"},{"indexed":true,"internalType":"address","name":"toDelegate","type":"address"}],"name":"DelegateChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"delegate","type":"address"},{"indexed":false,"internalType":"uint256","name":"previousBalance","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newBalance","type":"uint256"}],"name":"DelegateVotesChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINT_CAP_DENOMINATOR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MINT_CAP_NUMERATOR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MIN_MINT_INTERVAL","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint32","name":"pos","type":"uint32"}],"name":"checkpoints","outputs":[{"components":[{"internalType":"uint32","name":"fromBlock","type":"uint32"},{"internalType":"uint224","name":"votes","type":"uint224"}],"internalType":"struct ERC20VotesUpgradeable.Checkpoint","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"}],"name":"delegate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"delegateBySig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"delegates","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPastTotalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPastVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getVotes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1TokenAddress","type":"address"},{"internalType":"uint256","name":"_initialSupply","type":"uint256"},{"internalType":"address","name":"_owner","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"l1Address","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextMint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"numCheckpoints","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"transferAndCall","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]'


basic_vault_data = {
    "ETH": [
        "0x9014f8E90423766343Ed4fe41668563526dF6715", # Eth call - mainnet - weekly
        "0x6d2Cdb589BE6037Df1AeA5dC433829aD5aF30013", # Eth put - mainnet - weekly
        "0x60a4422B6B52aEF50647c67F29D6a7e6DAc3CCBC", # Btc call - mainnet - weekly
        "0x3BA337F3167eA35910E6979D5BC3b0AeE60E7d59", # Btc put - mainnet - weekly
    ],
    "BSC": [
        "0xF98297A842f52Cd1f6c6f5f003Cd701813b1C461", # Ada call - bsc - biweekly
        "0x8BE731cB3b301b4a209C1A38ea14D6438e6913F6", # Ada put - bsc - biweekly
        "0xc879ecC0d2cdA26072e9049178a99B26C51eDF8a", # Bch call - bsc - biweekly
        "0xfe9B8054B947aCEeC01912Cf1811DB06fc804b69", # Bch put - bsc - biweekly
        "0x9EF72De1782431cf54518c42C06e26014E7201D1", # Bnb call - bsc - biweekly
        "0xc75C3BE0Bc41857B9c1a675475F6E0a7c5Db63fC", # Bnb put - bsc - biweekly
    ],
    "ARBITRUM": [
        "0x0833EC3262Dcc417D88f85Ed5E1EBAf768080f41", # Arb call - arbitrum - biweekly
        "0xf94ea5B18401821BE07FBfF535B8211B061A7F70", # Arb put - arbitrum - biweekly
        "0x1D1CD4abe0F2AF9d79b5e3149BF4A503f97C1EAd", # Eth call - arbitrum - weekly
        "0x633A789BeD82215b1cEE45C32aCD0D6Ca8b9Bfbf", # Eth put - arbitrum - weekly
    ],
    "POLYGON": [
        "0x9dA79023Af00d1f2054BB1eED0D49004fe41C5b5", # Matic call - polygon - biweekly
        "0x1724B8679A9CaD6CABDef7DbEE1d5b03b44584B2", # Matic put - polygon - biweekly
    ],
    "FTM": [
        "0x302ABD505757FD355C8ef3cF8b4918D6404f4996", # FTM call - fantom - biweekly
        "0x7EDa4C29726355D0d8E85001B9152158b35Eae4f", # FTM put - fantom - biweekly
    ],
    "AVAXC": [
        "0xd06Bd68d58eD40CC2031238A3993b99172ea37cA", # Avalanche call - avax - biweekly
        "0xa84aA41B6287aFE467ccE688f3796A2205198F07", # Avalanche put - avax - biweekly
    ],
}

vault_expiry_data = []

for chain in basic_vault_data:
    for vault in basic_vault_data[chain]:
        print(vault)
        epoch_results = {}

        w3 = Web3(Web3.HTTPProvider(network_api[chain]))
        basic_vault_address = w3.to_checksum_address(vault)
        basic_vault = w3.eth.contract(address=basic_vault_address, abi=CashVault_ABI)

        epoch_results['name'] = basic_vault.functions.name().call()
        epoch_results['symbol'] = basic_vault.functions.symbol().call()

        current_vault_epoch = basic_vault.functions.epoch().call()
        current_expiry_timestamp = basic_vault.functions.epochExpiry(current_vault_epoch).call()
        current_strikeX1e6 = basic_vault.functions.strikeX1e6(current_vault_epoch).call()


        epoch_results['epoch'] = current_vault_epoch
        epoch_results['expiry'] = current_expiry_timestamp
        
        vault_expiry_data.append(epoch_results)

# print results
for data in vault_expiry_data:
    print(data['name'], data['epoch'], data['expiry'])
