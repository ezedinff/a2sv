'''
There are several days left before the fiftieth birthday of a famous Berland's writer Berlbury. In this connection the local library decided to make an exposition of the works of this famous science-fiction writer. It was decided as well that it is necessary to include into the exposition only those books that were published during a particular time period. It is obvious that if the books differ much in size, the visitors will not like it. That was why the organizers came to the opinion, that the difference between the highest and the lowest books in the exposition should be not more than k millimeters.

The library has n volumes of books by Berlbury, arranged in chronological order of their appearance. The height of each book in millimeters is know, it is hi. As Berlbury is highly respected in the city, the organizers want to include into the exposition as many books as possible, and to find out what periods of his creative work they will manage to cover. You are asked to help the organizers cope with this hard task.

Input
The first line of the input data contains two integer numbers separated by a space n (1 ≤ n ≤ 105) and k (0 ≤ k ≤ 106) — the amount of books by Berlbury in the library, and the maximum allowed height difference between the lowest and the highest books. The second line contains n integer numbers separated by a space. Each number hi (1 ≤ hi ≤ 106) is the height of the i-th book in millimeters.

Output
In the first line of the output data print two numbers a and b (separate them by a space), where a is the maximum amount of books the organizers can include into the exposition, and b — the amount of the time periods, during which Berlbury published a books, and the height difference between the lowest and the highest among these books is not more than k milllimeters.

In each of the following b lines print two integer numbers separated by a space — indexes of the first and the last volumes from each of the required time periods of Berlbury's creative work.

Examples
inputCopy
3 3
14 12 10
outputCopy
2 2
1 2
2 3
inputCopy
2 0
10 10
outputCopy
2 1
1 2
inputCopy
4 5
8 19 10 13
outputCopy
2 1
3 4

'''
'''
The main idea: to give a sequence of n elements, from which the longest sub-sequence
is selected, requiring that the maximum value of the element difference in the sub-sequence
not exceed K.
There are several eldest-son sequences, the length of the subsequence,
and the starting and ending positions of the subsequence.
Analysis: Not a monotonous queue of friends first look at my other blog post,
the topic follows the question is actually similar. (http://blog.csdn.net/maxichu/article/details/47612497)
we use a monotone queue to dynamically maintain the maximum and minimum values 
in the sequence. Before and after the establishment of the pointer I, J, once found that the front pointer to the maximum-minimum value >k, try to update the maximum value, and then J go forward, and so on.
on the code
'''

'''
The problem is to find the maximum number of books the organizers can include into the exposition, and the amount of the time periods during which Berlbury published books, and the height difference between the lowest and the highest among these books is not more than k millimeters. We are given the heights of n volumes of books by Berlbury, arranged in chronological order of their appearance.

To solve this problem, we can use a monotonic queue to dynamically maintain the maximum and minimum values in the sequence. We can use two deques, high and low, to maintain the highest and lowest values in the current subsequence of books. We use two pointers, i and j, to represent the end and start of the subsequence. We start by initializing i and j to 1.

We iterate over the sequence of books from left to right, and for each book, we update the deques high and low to maintain the maximum and minimum values in the current subsequence. If the difference between the maximum and minimum values in the subsequence is greater than k, we move the start pointer j to the right and update the deques high and low accordingly, until the difference between the maximum and minimum values in the subsequence is less than or equal to k. At each step, we update the answer by comparing the length of the current subsequence with the current maximum length, and we update the list of time periods accordingly.

Once we have processed all the books, we move the start pointer j to the right until it reaches the end of the sequence, and we update the answer and the list of time periods accordingly.'''

def read_input():
    n, k = map(int, input().split())
    books = list(map(int, input().split()))
    return n, k, books

def find_book_ranges(n, k, books):
    high = []
    low = []
    p = []
    i = j = ans = cnt = 0

    while i < n:
        while high and books[i] > high[-1]:
            high.pop()
        high.append(books[i])
        while low and books[i] < low[-1]:
            low.pop()
        low.append(books[i])

        while high and low and high[0] - low[0] > k:
            if books[j] == high[0]:
                high.pop(0)
            if books[j] == low[0]:
                low.pop(0)
            j += 1
        
        if i - j + 1 > ans:
            ans = i - j + 1
            cnt = 1
            p = [(j, i)]
        elif i - j + 1 == ans:
            cnt += 1
            p.append((j, i))
        i += 1

    return ans, cnt, p

def print_output(ans, cnt, p):
    print(ans, cnt)
    for start, end in p:
        print(start+1, end+1)

def main():
    n, k, books = read_input()
    ans, cnt, p = find_book_ranges(n, k, books)
    print_output(ans, cnt, p)

if __name__ == '__main__':
    main()




