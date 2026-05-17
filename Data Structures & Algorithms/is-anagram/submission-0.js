class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const dict = {}

        for (let i = 0; i < s.length; i++) {
            dict[s[i]] = dict[s[i]] ? dict[s[i]] + 1 : 1
        }

        for (let y = 0; y < t.length; y++) {
            if (dict[t[y]]) {
                dict[t[y]] -= 1
            } else {
                return false
            }
        }

        const result = Object.values(dict).filter(i => i === 1)

        return result.length > 0 ? false : true
    }
}
