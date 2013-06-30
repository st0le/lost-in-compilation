import java.util.Arrays;
import java.util.Random;

/**
 * User: st0le
 * Date: 6/27/13
 * Time: 12:13 AM
 */
public class FindTriplet {

    public static void main(String[] args) {
        new FindTriplet().solve();
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
        int[] A = randomArray(5, -15, 20);
        int[] B = randomArray(10, -15, 20);
        int[] C = randomArray(15, -15, 20);
        System.out.println(Arrays.toString(A));
        System.out.println(Arrays.toString(B));
        System.out.println(Arrays.toString(C));
        final int[] triplet = findTriplet_3(A, B, C);

        System.out.println(Arrays.toString(triplet));
    }

    // Complexity : O(n^3)
    private int[] findTriplet_1(int[] A, int[] B, int[] C) {
        Arrays.sort(C); //O(nlogn)

        for (int i = 0, il = A.length; i < il; i++) { // O(n^3)
            for (int j = 0, jl = B.length; j < jl; j++) {
                for (int k = 0, kl = C.length; k < kl; k++) {
                    int s = A[i] + B[j] + C[k];
                    if (s > 0) break; //prune the remaining
                    if (s == 0)
                        return new int[]{A[i], B[j], C[k]};
                }
            }
        }
        return null;
    }

    // Complexity : O(n^2 logn)
    private int[] findTriplet_2(int[] A, int[] B, int[] C) {
        Arrays.sort(C); // O(nlogn)
        for (int i = 0, l = A.length; i < l; i++) { // O(n^2 logn)
            for (int j = 0, jl = B.length; j < jl; j++) {
                int k = Arrays.binarySearch(C, -A[i] - B[j]); // O(logn)
                if (k >= 0) return new int[]{A[i], B[j], C[k]};
            }
        }
        return null;
    }

    // Complexity : O(n^2)
    private int[] findTriplet_3(int[] A, int[] B, int[] C) {
        //find out if an instance A[i] + B[j] + C[k] == 0 exists
        Arrays.sort(A); // O(nlogn)
        Arrays.sort(B); // O(nlogn)
        for (int i = 0; i < C.length; i++) { // O(n^2)
            int key = C[i];
            int left = 0, right = B.length - 1;

            while (left < A.length && right > 0) {
                int sum = key + A[left] + B[right];
                if (sum == 0) {
                    return new int[]{A[left], B[right], key};
                } else if (sum > 0) {
                    right--;
                } else {
                    left++;
                }
            }
        }
        return null;
    }
}
