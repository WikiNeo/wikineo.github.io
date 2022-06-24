---
title: '[LeetCode 211] Design Add and Search Words Data Structure'
published: true
tags: Trie
---

## Problem

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

### Example:

```shell
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

### Constraints:

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consist of `'.'` or lowercase English letters.
- There will be at most `3` dots in `word` for `search` queries.
- At most `10^4` calls will be made to `addWord` and `search`.

## Thoughts

- We can consider using `Trie` for word search problem

## TypeScript

```typescript
class TrieNode {
    children: Map<string, TrieNode>
    isEnd: boolean
    
    constructor(){
        this.children = new Map<string, TrieNode>()
        this.isEnd = false;
    }
    
}

class WordDictionary {
    root: TrieNode;
    
    constructor() {
        this.root = new TrieNode()
    }

    addWord(word: string): void {
        let cur: TrieNode = this.root;
        for(const c of word){
            if(!cur.children.has(c)) cur.children.set(c, new TrieNode())
            cur = cur.children.get(c)
        }
        cur.isEnd = true;
    }

    search(word: string): boolean {
        let res: boolean = false;
        const LEN: number = word.length
        let cur: TrieNode = this.root
        
        const exec = (i: number, node: TrieNode) => {
            if(res === true) return;
            if(i === LEN){
                if(node.isEnd === true) res = true
                return;
            }
            
            if(word[i] === '.') {
                for(const c of node.children.keys()){
                    exec(i + 1, node.children.get(c))
                }
            } else if(node.children.has(word[i])){
                exec(i + 1, node.children.get(word[i]))
            }
        }
        
        exec(0, cur)
        return res;
    }
}
```

## Reference

- [https://leetcode.com/problems/design-add-and-search-words-data-structure/](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
