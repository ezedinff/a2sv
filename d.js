// var MedianFinder = function () {
//     this.store = new MedianHeaps();
//   };
  
//   /**
//    * @param {number} num
//    * @return {void}
//    */
//   MedianFinder.prototype.addNum = function (num) {
//     this.store.add(num);
//   };
  
//   /**
//    * @return {number}
//    */
//   MedianFinder.prototype.findMedian = function () {
//     return this.store.getMedian();
//   };
  
//   class MedianHeaps {
//       constructor(minHeap = new Heap(), maxHeap = new Heap((a, b) => b - a),count=0) {
//           this.minHeap = minHeap;
//           this.maxHeap = maxHeap;
//           this.count = count
//         }
//     add(num) {
//       const top = this.minHeap.peek();
//       if (top <= num) {
//         this.minHeap.add(num, this.count++);
//       } else {
//         this.maxHeap.add(num, this.count++);
//       }
  
//       this.balance();
//     }
  
//     balance() {
//       if (this.maxHeap.size > this.minHeap.size) {
//         this.minHeap.add(...this.maxHeap.pop());
//       } else if (this.minHeap.size - this.maxHeap.size > 1) {
//         this.maxHeap.add(...this.minHeap.pop());
//       }
//     }
  
//     getMedian() {
//       if (this.maxHeap.size === this.minHeap.size) {
//         return (this.maxHeap.peek() + this.minHeap.peek()) / 2;
//       }
//       return this.minHeap.peek();
//     }
//   }
  
//   /**
//    * Your MedianFinder object will be instantiated and called as such:
//    * var obj = new MedianFinder()
//    * obj.addNum(num)
//    * var param_2 = obj.findMedian()
//    */
//   class Heap {
//     constructor(cmpFn, array = []) {
//       this.name = cmpFn == undefined ? "min" : "custom";
//       this.cmpFn = cmpFn || this.internalCmpFn;
//       this.tree = [];
//       this.size = 0;
//       this.count = 0;
//       this.idxMap = new Map();
//       this.idxRevMap = new Map();
//       for (let value of array) {
//         this.add(value);
//       }
//     }
//     _left(idx) {
//       return 2 * idx + 1;
//     }
//     _right(idx) {
//       return 2 * idx + 2;
//     }
//     _parent(idx) {
//       return ((idx - 1) / 2) >> 0;
//     }
//     _swap(i, j) {
//       let countI = this.idxMap.get(i);
//       let countJ = this.idxMap.get(j);
//       let idxI = this.idxRevMap.get(countI);
//       let idxJ = this.idxRevMap.get(countJ);
//       this.idxMap.set(i, countJ);
//       this.idxMap.set(j, countI);
//       this.idxRevMap.set(countI, j);
//       this.idxRevMap.set(countJ, i);
//       [this.tree[i], this.tree[j]] = [this.tree[j], this.tree[i]];
//     }
  
//     internalCmpFn(value1, value2) {
//       return value1 - value2;
//     }
//     _heapifyUp(idx) {
//       let parent = this._parent(idx);
//       while (parent != idx && this.cmpFn(this.tree[idx], this.tree[parent]) < 0) {
//         this._swap(idx, parent);
//         idx = parent;
//         parent = this._parent(idx);
//       }
//     }
  
//     add(value, count) {
//       count = count == undefined ? this.count : count;
//       this.tree[this.size] = value;
//       this.idxMap.set(this.size, count);
//       this.idxRevMap.set(count, this.size);
//       let idx = this.size;
//       this._heapifyUp(idx);
//       this.size++;
//       this.count++;
//     }
  
//     heapify(idx) {
//       let left = this._left(idx);
//       let right = this._right(idx);
//       let current = idx;
//       if (left < this.size && this.cmpFn(this.tree[left], this.tree[idx]) < 0) {
//         current = left;
//       }
//       if (
//         right < this.size &&
//         this.cmpFn(this.tree[right], this.tree[current]) < 0
//       ) {
//         current = right;
//       }
//       if (current != idx) {
//         this._swap(idx, current);
//         this.heapify(current);
//       }
//     }
  
//     pop() {
//       if (this.size == 0) {
//         return null;
//       }
//       let value = this.tree[0];
//       let count = this.idxMap.get(0);
//       this._swap(0, this.size - 1);
//       this.size--;
//       this.tree.length = this.size;
//       this.heapify(0);
//       this.idxRevMap.delete(count);
//       this.idxMap.delete(this.size);
//       return [value, count];
//     }
  
//     popAt(count) {
//       if (!this.idxRevMap.has(count) || this.size == 0) {
//         return null;
//       }
//       let idx = this.idxRevMap.get(count);
//       let value = this.tree[idx];
//       this._swap(idx, this.size - 1);
//       this.size--;
//       this.tree.length = this.size;
//       this.heapify(idx);
//       this._heapifyUp(idx);
//       this.idxRevMap.delete(count);
//       this.idxMap.delete(this.size);
//       return [value, count];
//     }
  
//     peek() {
//       return this.tree[0];
//     }
//   }


// /*
// https://leetcode.com/problems/find-median-from-data-stream/

// convert to typescript code
// */

// class MedianFinder {
//   constructor() {
//     this.minHeap = new Heap();
//     this.maxHeap = new Heap((a, b) => b - a);
//   }

//   addNum(num: number): void {
//     const top = this.minHeap.peek();
//     if (top <= num) {
//       this.minHeap.add(num);
//     } else {
//       this.maxHeap.add(num);
//     }

//     this.balance();
//   }

//   balance(): void {
//     if (this.maxHeap.size > this.minHeap.size) {
//       this.minHeap.add(...this.maxHeap.pop());
//     } else if (this.minHeap.size - this.maxHeap.size > 1) {
//       this.maxHeap.add(...this.minHeap.pop());
//     }
//   }

//   findMedian(): number {
//     if (this.maxHeap.size === this.minHeap.size) {
//       return (this.maxHeap.peek() + this.minHeap.peek()) / 2;
//     }
//     return this.minHeap.peek();
//   }
// }

// class Heap {
//   tree: number[];
//   cmpFn: (a: number, b: number) => number;
//   size: number;
//   count: number;
//   idxMap: Map<number, number>;
//   idxRevMap: Map<number, number>;

//   constructor(cmpFn?: (a: number, b: number) => number, array?: number[]) {
//     this.cmpFn = cmpFn || this.internalCmpFn;
//     this.tree = [];
//     this.size = 0;
//     this.count = 0;
//     this.idxMap = new Map();
//     this.idxRevMap = new Map();
//     for (let value of array || []) {
//       this.add(value);
//     }
//   }

//   _left(idx: number): number {
//     return 2 * idx + 1;
//   }

//   _right(idx: number): number {
//     return 2 * idx + 2;
//   }

//   _parent(idx: number): number {
//     return ((idx - 1) / 2) >> 0;
//   }

//   _swap(i: number, j: number): void {
//     const countI = this.idxMap.get(i);
//     const countJ = this.idxMap.get(j);
//     const idxI = this.idxRevMap.get(countI);
//     const idxJ = this.idxRevMap.get(countJ);
//     this.idxMap.set(i, countJ);
//     this.idxMap.set(j, countI);
//     this.idxRevMap.set(countI, j);
//     this.idxRevMap.set(countJ, i);
//     [this.tree[i], this.tree[j]] = [this.tree[j], this.tree[i]];
//   }

//   internalCmpFn(value1: number, value2: number): number {
//     return value1 - value2;
//   }

//   _heapifyUp(idx: number): void {
//     let parent = this._parent(idx);
//     while (parent != idx && this.cmpFn(this.tree[idx], this.tree[parent]) < 0) {
//       this._swap(idx, parent);
//       idx = parent;
//       parent = this._parent(idx);
//     }
//   }

//   add(value: number, count?: number): void {
//     count = count == undefined ? this.count : count;
//     this.tree[this.size] = value;
//     this.idxMap.set(this.size, count);
//     this.idxRevMap.set(count, this.size);
//     let idx = this.size;
//     this._heapifyUp(idx);
//     this.size++;
//     this.count++;
//   }

//   heapify(idx: number): void {
//     let left = this._left(idx);
//     let right = this._right(idx);
//     let current = idx;
//     if (left < this.size && this.cmpFn(this.tree[left], this.tree[idx]) < 0) {
//       current = left;
//     }
//     if (
//       right < this.size &&
//       this.cmpFn(this.tree[right], this.tree[current]) < 0
//     ) {
//       current = right;
//     }
//     if (current != idx) {
//       this._swap(idx, current);
//       this.heapify(current);
//     }
//   }

//   pop(): [number, number] {
//     if (this.size == 0) {
//       return null;
//     }
//     let value = this.tree[0];
//     let count = this.idxMap.get(0);
//     this._swap(0, this.size - 1);
//     this.size--;
//     this.tree.length = this.size;
//     this.heapify(0);
//     this.idxRevMap.delete(count);
//     this.idxMap.delete(this.size);
//     return [value, count];
//   }

//   popAt(count: number): [number, number] {
//     if (!this.idxRevMap.has(count) || this.size == 0) {
//       return null;
//     }
//     let idx = this.idxRevMap.get(count);
//     let value = this.tree[idx];
//     this._swap(idx, this.size - 1);
//     this.size--;
//     this.tree.length = this.size;
//     this.heapify(idx);
//     this._heapifyUp(idx);
//     this.idxRevMap.delete(count);
//     this.idxMap.delete(this.size);
//     return [value, count];
//   }

//   peek(): number {
//     return this.tree[0];
//   }
// }

