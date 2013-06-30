import java.util.Arrays;
import java.util.HashSet;
import java.util.Random;
import java.util.Set;

/**
 * User: st0le
 * Date: 6/29/13
 * Time: 5:47 PM
 */
public class TwoSum {
    public static void main(String[] args) {
        new TwoSum().solve();
    }

    public int[] randomArray(int sz, int lo, int hi) {
        Random r = new Random();
        final int[] arr = new int[sz];
        for (int i = 0; i < sz; i++) {
            arr[i] = r.nextInt(hi - lo) + lo;
        }
        return arr;
    }

    public void solve() {
        int[] A = randomArray(10, -15, 20);
        System.out.println(Arrays.toString(A));
        final int[] duo = findPair_2(A);
        System.out.println(Arrays.toString(duo));
    }

    // Complexity - O(n^2)
    private int[] findPair_1(int[] A) {
        Arrays.sort(A); // O(nlogn)
        for (int i = 0, l = A.length; i < l; i++) {
            for (int j = i + 1; j < l; j++) {
                int s = A[i] + A[j];
                if (s > 0) break;
                if (s == 0) return new int[]{A[i], A[j]};
            }
        }
        return null;
    }

    // Complexity - O(nlogn)
    private int[] findPair_2(int[] A) {
        Arrays.sort(A); // O(nlogn)
        for (int i = 0, l = A.length; i < l; i++) { //O(nlogn)
            int j = Arrays.binarySearch(A, i + 1, l, -A[i]);
            if (j > i) return new int[]{A[i], A[j]};
        }
        return null;
    }

    // Complexity - O(n), Space Complexity - O(n)
    private int[] findPair_3(int[] A) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0, l = A.length; i < l; i++) {
            if (set.contains(-A[i]))
                return new int[]{A[i], -A[i]};
            else
                set.add(A[i]);
        }
        return null;
    }

    // If Array was already sorted
    // Complexity - O(n)
    private int[] findPair_4(int[] A) {
        int left = 0, right = A.length - 1;
        while (left < right) {
            int s = A[left] + A[right];
            if (s == 0)
                return new int[]{A[left], A[right]};
            else if (s > 0)
                right--;
            else
                left++;
        }
        return null;
    }
}
