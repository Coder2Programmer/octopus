from octopus.platforms.ETH.explorer import EthereumInfuraExplorer
from octopus.config.ETH_EXPLORER import INFURA_ROPSTEN

# connection to ROPSTEN network (testnet)
explorer = EthereumInfuraExplorer("bHuaQhX91nkQBac8Wtgj",
                                  network=INFURA_ROPSTEN)
# connection to MAINNET network (mainnet)
# explorer = EthereumInfuraExplorer("bHuaQhX91nkQBac8Wtgj")

# test infura access
block_number = explorer.eth_blockNumber()
print('blockNumber = %d' % block_number)

# retrieve code of this smart contract
addr = "0x3c6B10a5239B1a8A27398583F49771485382818F"
code = explorer.eth_getCode(addr)
print('code = %s' % code)