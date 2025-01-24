import java.util.Scanner;

public class StockConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String priceInput = scanner.nextLine();
        String rateInput = scanner.nextLine();
        
        System.out.println("Price Input: " + priceInput); 
        System.out.println("Rate Input: " + rateInput);  
    
        double price = parseAmount(priceInput);
        double rate = Double.parseDouble(rateInput); 
        
        System.out.println("Parsed Price: " + price); 
        System.out.println("Parsed Rate: " + rate);  
        
        double convertedPrice = price * rate;
        
        System.out.println(convertedPrice);
    }
    
    private static double parseAmount(String input) {
        String cleaned = input.replaceAll("[^0-9.]", "");
        if (cleaned.isEmpty()) {
            return 0.0;
        }
        return Double.parseDouble(cleaned);
    }
}