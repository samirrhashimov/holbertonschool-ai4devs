public class Bug3 {

    // Checks if the entered password matches the stored one
    public static boolean isPasswordCorrect(String input, String stored) {
        // BUG: == compares references, not string content
        return input == stored;
    }

    public static void main(String[] args) {
        String stored = "secret123";
        String input = new String("secret123");

        if (isPasswordCorrect(input, stored)) {
            System.out.println("Access granted");
        } else {
            System.out.println("Access denied");
        }
    }
}