import java.util.Arrays;
import java.util.Comparator;
import java.util.Random;

/**
 * User: st0le
 * Date: 7/1/13
 * Time: 4:57 PM
 */
public class FindQuadruplet {

    public static void main(String[] args) {
        new FindQuadruplet().solve();
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
        int[] D = randomArray(15, -15, 20);
        System.out.println(Arrays.toString(A));
        System.out.println(Arrays.toString(B));
        System.out.println(Arrays.toString(C));
        System.out.println(Arrays.toString(D));
        final int[] quad = findQuad_3(A, B, C, D);
        System.out.println(Arrays.toString(quad));
    }

    // Complexity - O(n^4)
    private int[] findQuad_1(int[] A, int[] B, int[] C, int[] D) {
        for (int i = 0, al = A.length; i < al; i++)
            for (int j = 0, bl = B.length; j < bl; j++)
                for (int k = 0, cl = C.length; k < cl; k++)
                    for (int l = 0, dl = D.length; l < dl; l++)
                        if (A[i] + B[j] + C[k] + D[l] == 0) return new int[]{A[i], B[j], C[k], D[l]};
        return null;
    }

    // Complexity - O(n^3 logn)
    private int[] findQuad_2(int[] A, int[] B, int[] C, int[] D) {
        Arrays.sort(D);
        for (int i = 0, al = A.length; i < al; i++) {
            for (int j = 0, bl = B.length; j < bl; j++) {
                for (int k = 0, cl = C.length; k < cl; k++) {
                    int l = Arrays.binarySearch(D, -(A[i] + B[j] + C[k]));
                    if (l >= 0) return new int[]{A[i], B[j], C[k], D[l]};
                }
            }
        }
        return null;
    }

    // Complexity - O(n^3)
    private int[] findQuad_3(int[] A, int[] B, int[] C, int[] D) {
        Arrays.sort(C);
        Arrays.sort(D);
        int cl = C.length, dl = D.length;
        for (int i = 0, al = A.length; i < al; i++) {
            for (int j = 0, bl = B.length; j < bl; j++) {
                int left = 0, right = dl - 1;
                while (left < cl && right >= 0) {
                    int s = A[i] + B[j] + C[left] + D[right];
                    if (s == 0)
                        return new int[]{A[i], B[j], C[left], D[right]};
                    if (s < 0)
                        left++;
                    else
                        right--;
                }
            }
        }
        return null;
    }

    // Complexity - O(n^2), Space Complexity - O(n^2)
    private int[] findQuad_4(int[] A, int[] B, int[] C, int[] D) {
        Integer[] AB = new Integer[A.length * B.length];
        Integer[] CD = new Integer[C.length * D.length];
        for (int i = 0, l = AB.length; i < l; i++) AB[i] = i;
        for (int i = 0, l = CD.length; i < l; i++) CD[i] = i;

        Arrays.sort(AB, new IndexComparator(A, B));
        Arrays.sort(CD, new IndexComparator(C, D));

        int left = 0, abl = AB.length, right = CD.length - 1;
        int bl = B.length, dl = D.length;
        while (left < abl && right >= 0) {
            int leftIndex = AB[left], rightIndex = CD[right];
            int s = A[leftIndex / bl] + B[leftIndex % bl] + C[rightIndex / dl] + D[rightIndex % dl];
            if (s == 0)
                return new int[]{A[leftIndex / bl], B[leftIndex % bl], C[rightIndex / dl], D[rightIndex % dl]};
            else if (s < 0)
                left++;
            else
                right--;
        }
        return null;
    }

    private class IndexComparator implements Comparator<Integer> {

        private int[] X, Y;
        private int yl;

        private IndexComparator(int[] x, int[] y) {
            X = x;
            Y = y;
            yl = Y.length;
        }

        @Override
        public int compare(Integer o1, Integer o2) {
            return X[o1 / yl] + Y[o1 % yl] <= X[o2 / yl] + Y[o2 % yl] ? -1 : 1;
        }
    }

}
