function medianSlidingWindow(nums: number[], k: number): number[] {
  const result: number[] = []
  const window = nums.slice(0, k)
  window.sort((a, b) => a - b)
  const sortWindow = (removedNum: number, insertedNum: number) => {
    const removedIndex = window.findIndex(num => removedNum === num)
    window.splice(removedIndex, 1)
    const insertedIndex = window.findIndex(num => insertedNum < num)
    if (insertedIndex === -1) {
      window.push(insertedNum)
    } else {
      window.splice(insertedIndex, 0, insertedNum)
    }
  }
  const getMedian = () => {
    const middle = Math.floor((window.length - 1) / 2)
    if (window.length % 2 === 1) {
      return window[middle]
    }
    return (window[middle] + window[middle + 1]) / 2
  }
  result.push(getMedian())
  for (let i = 1; i < nums.length - k + 1; i++) {
    sortWindow(nums[i - 1], nums[i + k - 1])
    result.push(getMedian())
  }
  return result
}