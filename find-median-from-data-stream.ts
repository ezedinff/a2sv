/*
https://leetcode.com/problems/find-median-from-data-stream/
*/

// using min heap and max heap
// min heap stores the larger half of the numbers
// max heap stores the smaller half of the numbers
// the size of the two heaps are balanced or differ by 1
// the median is the top of the heap with more elements
class Heap {
    pop() {
        throw new Error("Method not implemented.");
    }
    tree: number[];
    cmpFn: (a: number, b: number) => number;
    size: number;
    count: number;
    idxMap: Map<number, number>;
    idxRevMap: Map<number, number>;
  
    constructor(cmpFn?: (a: number, b: number) => number, array?: number[]) {
      this.cmpFn = cmpFn || this.internalCmpFn;
      this.tree = [];
      this.size = 0;
      this.count = 0;
      this.idxMap = new Map();
      this.idxRevMap = new Map();
      for (let value of array || []) {
        this.add(value);
      }
    }
    
    internalCmpFn(a: number, b: number): number {
        return a - b;
    }

    add(value: number): void {
        this.tree.push(value);
        this.size++;
        this.count++;
        this.idxMap.set(value, this.count);
        this.idxRevMap.set(this.count, value);
        this.bubbleUp(this.size - 1);
    }

    remove(): number | null {
        if (this.size === 0) {
            return null;
        }
        let value = this.tree[0];
        this.swap(0, this.size - 1);
        this.tree.pop();
        this.size--;
        this.count++;
        this.idxMap.delete(value);
        this.idxRevMap.delete(this.count);
        this.bubbleDown(0);
        return value;
    }

    bubbleUp(idx: number): void {
        if (idx === 0) {
            return;
        }
        let parent = Math.floor((idx - 1) / 2);
        if (this.cmpFn(this.tree[idx], this.tree[parent]) < 0) {
            this.swap(idx, parent);
            this.bubbleUp(parent);
        }
    }

    bubbleDown(idx: number): void {
        let left = idx * 2 + 1;
        let right = idx * 2 + 2;
        let min = idx;
        if (left < this.size && this.cmpFn(this.tree[left], this.tree[min]) < 0) {
            min = left;
        }
        if (right < this.size && this.cmpFn(this.tree[right], this.tree[min]) < 0) {
            min = right;
        }
        if (min !== idx) {
            this.swap(idx, min);
            this.bubbleDown(min);
        }
    }

    swap(idx1: number, idx2: number): void {
        let tmp = this.tree[idx1];
        this.tree[idx1] = this.tree[idx2];
        this.tree[idx2] = tmp;
        this.idxMap.set(this.tree[idx1], idx1 + 1);
        this.idxMap.set(this.tree[idx2], idx2 + 1);
        this.idxRevMap.set(idx1 + 1, this.tree[idx1]);
        this.idxRevMap.set(idx2 + 1, this.tree[idx2]);
    }

    peek(): number | null {
        if (this.size === 0) {
            return null;
        }
        return this.tree[0];
    }

    removeNum(num: number): void {
        let idx = this.idxMap.get(num);
        if (idx === undefined) {
            return;
        }
        idx--;
        this.swap(idx, this.size - 1);
        this.tree.pop();
        this.size--;
        this.count++;
        this.idxMap.delete(num);
        this.idxRevMap.delete(this.count);
        this.bubbleDown(idx);
    }

    toString(): string {
        return this.tree.toString();
    }

    toArray(): number[] {
        return this.tree;
    }
 }
  
class MedianFinder {
    minHeap: Heap;
    maxHeap: Heap;
    count: number;
    constructor() {
        this.minHeap = new Heap();
        this.maxHeap = new Heap((a, b) => b - a);
        this.count = 0;
    }

    addNum(num: number): void {
        this.count++;
        if (this.count % 2 === 1) {
            this.maxHeap.add(num);
        } else {
            this.minHeap.add(num);
        }
        if (this.minHeap.peek() !== null && this.maxHeap.peek() !== null && this.minHeap.peek() < this.maxHeap.peek()) {
            let min = this.minHeap.remove();
            let max = this.maxHeap.remove();
            this.minHeap.add(max);
            this.maxHeap.add(min);
        }
    }

    findMedian(): number | null {
        if (this.count % 2 === 1) {
            return this.maxHeap.peek();
        } else {
            return (this.minHeap.peek() + this.maxHeap.peek()) / 2;
        }
    }
}