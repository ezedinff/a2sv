function arrayManipulation(n: number, queries: number[][]): number {
    const arr = new Array(n+1).fill(0);
    for (const [a, b, k] of queries) {
        arr[a-1] += k;
        arr[b] -= k;
    }
    let max_val = 0;
    let curr = 0;
    for (const i of arr) {
        curr += i;
        max_val = Math.max(max_val, curr);
    }
    return max_val;
}

function minimumPasses(m: number, w: number, p: number, n: number): number {
    let days = 0;
    let candies = 0;
    let answer = Math.ceil(n / (m * w));
    while (days < answer) {
        if (p > candies) {
            const daysNeeded = Math.ceil((p - candies) / (m * w));
            candies += daysNeeded * m * w;
            days += daysNeeded;
        }
        const diff = Math.abs(m - w);
        const available = Math.floor(candies / p);
        const purchased = Math.min(available, diff);
        if (m > w) {
            w += purchased;
        } else {
            m += purchased;
        }
        const rest = available - purchased;
        m += Math.floor(rest / 2);
        w += rest - Math.floor(rest / 2);
        candies -= available * p;

        candies += m * w;
        days += 1;

        answer = Math.min(answer, days + Math.ceil((n - candies) / (m * w)));
    }
    return answer;
}
//
let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;;

function readLine(): string {
    return inputLines[currentLine++];
}

function main() {
    const t = parseInt(readLine(), 10);
    for (let tItr = 0; tItr < t; tItr++) {
        const nm = readLine().split(' ');
        const n = parseInt(nm[0], 10);
        const m = parseInt(nm[1], 10);
        const edges = Array(m);
        for (let i = 0; i < m; i++) {
            edges[i] = readLine().split(' ').map(edgesTemp => parseInt(edgesTemp, 10));
        }
        const s = parseInt(readLine(), 10);
        const result = bfs(n, m, edges, s);
        console.log(result.join(" "));
    }   
}

function bfs(n: number, m: number, edges: number[][], s: number): number[] {
    const graph = new Map<number, number[]>();
    for (const [a, b] of edges) {
        if (!graph.has(a)) {
            graph.set(a, []);
        }
        if (!graph.has(b)) {
            graph.set(b, []);
        }
        graph.get(a)?.push(b);
        graph.get(b)?.push(a);
    }
    const queue = [s];
    const visited = new Set<number>();
    const distance = new Map<number, number>();
    distance.set(s, 0);
    while (queue.length > 0) {
        const node = queue.shift()!;
        visited.add(node);
        for (const neighbor of graph.get(node) ?? []) {
            if (!visited.has(neighbor)) {
                queue.push(neighbor);
                distance.set(neighbor, (distance.get(node) ?? 0) + 6);
            }
        }
    }
    const result: number[] = [];
    for (let i = 1; i <= n; i++) {
        if (i === s) {
            continue;
        }
        result.push(distance.get(i) ?? -1);
    }
    return result;
}