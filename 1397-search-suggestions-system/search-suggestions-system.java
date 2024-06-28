class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products);
        List<List<String>> res = new LinkedList<>();
        String s = "";
        for (int i = 0; i < searchWord.length(); i++) {
            List<String> l = new LinkedList<>();
            s += searchWord.charAt(i);
            int idx = Arrays.binarySearch(products, s, (a, b) -> a.compareTo(b));
            idx = idx < 0 ? -1 * idx - 1 : idx;
            for (int j = 0; j < 3; j++)
                if (idx + j < products.length && products[idx + j].startsWith(s))
                    l.add(products[idx + j]);
            res.add(l);
        }
        return res;
    }
}