import java.math.BigInteger;
class Solution {
    public String addStrings(String num1, String num2) {
        BigInteger bigInteger1 = new BigInteger(num1);
        BigInteger bigInteger2 = new BigInteger(num2);
        BigInteger res = bigInteger1.add(bigInteger2);
        String s = String.valueOf(res);
        return s;
    }
}
