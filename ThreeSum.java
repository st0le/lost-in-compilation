import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

/**
 * User: st0le
 * Date: 6/29/13
 * Time: 7:10 PM
 */
public class ThreeSum {
    public static void main(String[] args) {
        new ThreeSum().solve();
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
        final int[] duo = findTriple_3(A);
        System.out.println(Arrays.toString(duo));
    }

    // Complexity - O(n^3)
    private int[] findTriple_1(int[] A) {
        Arrays.sort(A); // O(nlogn)
        for (int i = 0, l = A.length; i < l && A[i] < 0; i++) {
            for (int j = i + 1; j < l && A[i] + A[j] < 0; j++) {
                for (int k = j + 1; k < l; k++) {
                    int s = A[i] + A[j] + A[k];
                    if (s > 0) break;
                    if (s == 0) return new int[]{A[i], A[j], A[k]};
                }
            }
        }
        return null;
    }

    // Complexity - O(n^2 logn)
    private int[] findTriple_2(int[] A) {
        Arrays.sort(A); // O(nlogn)
        for (int i = 0, l = A.length; i < l && A[i] < 0; i++) { //O(nlogn)
            for (int j = i + 1; j < l && A[i] + A[j] < 0; j++) {
                int k = Arrays.binarySearch(A, j + 1, l, -A[i] - A[j]);
                if (k > j) return new int[]{A[i], A[j], A[k]};
            }
        }
        return null;
    }

    // Complexity - O(n^2), Space Complexity - O(n^2)
    private int[] findTriple_3(int[] A) {
        Map<Integer, int[]> map = new HashMap<Integer, int[]>();
        for (int i = 0, l = A.length; i < l; i++) {
            map.clear();
            for (int j = i + 1; j < l; j++) {
                if (map.containsKey(A[j])) {
                    int[] pair = map.get(A[j]);
                    return new int[]{pair[0], pair[1], A[j]};
                } else
                    map.put(-A[i] - A[j], new int[]{A[i], A[j]});
            }
        }
        return null;
    }

    // Complexity - O(n^2)
    private int[] findTriple_4(int[] A) {
        Arrays.sort(A);
        for (int i = 0,l = A.length; i < l; i++) {
            int left = i + 1, right = l - 1;
            while (left < right) {
                int s = A[i] + A[left] + A[right];
                if (s == 0)
                    return new int[]{A[i],A[left], A[right]};
                else if (s > 0)
                    right--;
                else
                    left++;
            }
        }
        return null;
    }

}
