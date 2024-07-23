class Solution {
    class Edge implements Comparable<Edge> {
        int no;
        int freq;

        Edge(int n,int f)
        {
            this.no=n;
            this.freq=f;
        }


        @Override
        public int compareTo(Edge o) {
            if(this.freq!=o.freq)
            {
                return this.freq-o.freq;
            }
            else {
                return o.no-this.no;
            }

        }
    }
    public int[] frequencySort(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
       
        Arrays.sort(nums);
        PriorityQueue<Edge> pq=new PriorityQueue<>();
        for(int num:nums)
        {
            map.put(num,map.getOrDefault(num,0)+1);
        }

       for(int i=0;i<nums.length;)
       {
           int freq=map.get(nums[i]);
           pq.add(new Edge(nums[i],freq));
           i+=freq;
       }


      int index=0;
       while(!pq.isEmpty())
       {
           int f=0;
           Edge e=pq.remove();
           int n=e.no;
           while(f<e.freq)
           {
               nums[index]=n;
               f++;
               index++;
           }


       }
       
    
        return (nums);
    }
}