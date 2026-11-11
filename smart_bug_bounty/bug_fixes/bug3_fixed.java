import java.util.Objects;

public class Bug3Fixed {

    // Checks if the entered password matches the stored one
    public static boolean isPasswordCorrect(String input, String stored) {
        // FIX: compare content with equals (null-safe), not references with ==
        return Objects.equals(input, stored);
    }

    public static void main(String[] args) {
        String stored = "secret123";

        System.out.println(isPasswordCorrect(new String("secret123"), stored)); // true
        System.out.println(isPasswordCorrect("wrong", stored));                 // false
        System.out.println(isPasswordCorrect(null, stored));                    // false
    }
}