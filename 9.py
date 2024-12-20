from enum import Enum   
from typing import Optional

input = "2333133121414131402"

def main():
    input = open("9.input").read()
    print(part1(input))
    print(part2(input))

class BlockType(Enum):
    FREE = 1
    USED = 2

class Block:
    def __init__(self, block_type: BlockType, space: int, id: Optional[int] = None):
        self.type = block_type
        self.space = space
        self.id = id
    def block_string(self):
        if self.type == BlockType.FREE:
            return "." * self.space
        else:
            return str(self.id) *  self.space
    def block_array(self):
        if self.type == BlockType.FREE:
            return ["." for space in range(self.space)]
        else:
            return [str(self.id) for space in range(self.space)]

    def __repr__(self):
        return f"Block(type={self.type.name}, space={self.space}, id={self.id})"

def get_complex_block_array(input):
    blocks: list[Block] = []
    type = 0
    block_id = 0
    for block in input:
        if type==0:
            blocks.append(Block(BlockType.USED, int(block), block_id))
            type = 1
            block_id+=1
        else:
            blocks.append(Block(BlockType.FREE, int(block)))
            type = 0
    return blocks

def get_simple_block_array(input):
    blocks: list[Block] = []
    type = 0
    block_id = 0
    for block in input:
        if type==0:
            for i in range(int(block)):
                blocks.append(str(block_id))
            type = 1
            block_id+=1
        else:
            for i in range(int(block)):
                blocks.append(".")
            type = 0
    return blocks

def part2(input):
    blocks = get_complex_block_array(input)
    block_array = move_blocks_complex(blocks)
    block_str = [x for block in block_array for x in block.block_array()]
    return sum([i * int(block_str[i]) for i in range(len(block_str)) if block_str[i] != "."])

def part1(input):
    blocks = get_simple_block_array(input)
    block_array = move_blocks_simple(blocks)
    return sum([i * int(block_array[i]) for i in range(len(block_array)) if block_array[i] != "."])

def move_blocks_complex(block_str: list[Block]):
    for i in range(len(block_str) - 1, -1, -1):
        data_block = block_str[i]
        if data_block.type == BlockType.FREE:
            continue
        for j in range(len(block_str)):
                if i == j: break
                free_block = block_str[j]
                if free_block.type != BlockType.FREE:
                    continue
                if free_block.space < data_block.space:
                    continue
                if free_block.space == data_block.space:
                    block_str[i] = free_block
                    block_str[j] = data_block
                    break
                if free_block.space > data_block.space:
                    block_str[i] = Block(BlockType.FREE, data_block.space)
                    block_str[j] = Block(BlockType.USED, data_block.space, data_block.id)
                    block_str.insert(j+1, Block(BlockType.FREE, free_block.space - data_block.space))
                    break
    return block_str

def move_blocks_simple(block_string: list[str]):
    for i in range(len(block_string)):
        if block_string[i] != ".":
            continue
        for j in range(len(block_string) - 1, -1, -1):
            if (i == j):
                return block_string
            if block_string[j] == ".":
                continue
            else:
                block_string[i] = block_string[j]
                block_string[j] = "."
                break
    return block_string

main()