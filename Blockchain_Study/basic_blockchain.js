
//Creating a basic Blockchain
const SHA256 = require('crypto-js/sha256');

class Block{
	constructor(index, timestamp, data, previous_hash = ""){

		this.index = index;
		this.timestamp = timestamp;
		this.data = data;
		this.previous_hash = previous_hash;
		this.hash = this.calculate_hash();
	}

	calculate_hash(){

		return SHA256(this.index + this.previous_hash + this.timestamp + JSON.stringify(this.data)).toString();
	}

}

class Blockchain{
	constructor(){

		this.chain = [this.createGenesisBlock()];
	}

	createGenesisBlock(){
		return new Block(0, "01/01/2020", "Genesis block", "0");

	}

	getLatestBlock(){
		return this.chain[this.chain.length -1];
	}

	addBlock(newBlock){
		newBlock.previous_hash = this.getLatestBlock().hash;
		newBlock.hash = newBlock.calculate_hash();
		this.chain.push(newBlock);
	}

	isChainValid(){
		for(let i = 1; i < this.chain.length; i++){
			const currentBlock = this.chain[i];
			const previousBlock = this.chain[i-1];

			if (currentBlock.hash !== currentBlock.calculate_hash()){
				return false;
			}
			if (currentBlock.previous_hash !== previousBlock.hash){
				return false;
			}
		}

		return true;

	}
}

let devrCoin = new Blockchain();
devrCoin.addBlock(new Block(1, "10/10/2020", {amount: 4}));
devrCoin.addBlock(new Block(2, "12/10/2020", {amount: 10}));

console.log("Is blockchain valid? " + devrCoin.isChainValid());
//console.log(JSON.stringify(devrCoin, null, 4));




