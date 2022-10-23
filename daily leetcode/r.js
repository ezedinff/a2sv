function recursiveStringReverse(string) {
    if (string.length <= 1) {
        return string;
    }

    const f = string[0];
    const l = string[string.length - 1];

    return l + recursiveStringReverse(string.slice(1, string.length - 1)) + f;
}