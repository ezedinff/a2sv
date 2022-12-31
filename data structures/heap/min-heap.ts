export default class MinHeap {
    public heap: number[] = [];
    public length: number = 0;
    insert(value: number): void {
        this.heap.push(value);
        this.length++;
        this.bubbleUp();
    }
    extractMin(): number {
        const min = this.heap[0];
        this.heap[0] = this.heap[this.length - 1];
        this.heap.pop();
        this.length--;
        this.bubbleDown();
        return min;
    }
    bubbleUp(): void {
        let index = this.length - 1;
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[index] < this.heap[parentIndex]) {
                [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
                index = parentIndex;
            } else {
                break;
            }
        }
    }
    bubbleDown(): void {
        let index = 0;
        while (index < this.length) {
            const leftIndex = index * 2 + 1;
            const rightIndex = index * 2 + 2;
            let minIndex = index;
            if (leftIndex < this.length && this.heap[leftIndex] < this.heap[minIndex]) {
                minIndex = leftIndex;
            }
            if (rightIndex < this.length && this.heap[rightIndex] < this.heap[minIndex]) {
                minIndex = rightIndex;
            }
            if (minIndex !== index) {
                [this.heap[index], this.heap[minIndex]] = [this.heap[minIndex], this.heap[index]];
                index = minIndex;
            } else {
                break;
            }
        }
    }
    remove(index: number): void {
        this.heap[index] = this.heap[this.length - 1];
        this.heap.pop();
        this.length--;
        this.bubbleDown();
    }
}
