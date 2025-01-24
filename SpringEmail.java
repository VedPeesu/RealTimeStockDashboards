import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.event.EventListener;
import org.springframework.boot.context.event.ApplicationReadyEvent;

@SpringBootApplication
public class SpringEmail {

    @Autowired
    private EmailSenderService emailSenderService;

    @Autowired
    private NewsService newsService;

    public static void main(String[] args) {
        SpringApplication.run(SpringEmail.class, args);
    }

    @EventListener(ApplicationReadyEvent.class)
    public void sendEconomicNews() {
        String economicNews = newsService.fetchEconomicNews();

        emailSenderService.sendEmail(
            "recipient_email@changeemail.com",  
            "Today's Economic News",      
            economicNews
        );
    }
}
