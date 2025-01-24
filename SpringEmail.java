import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.event.EventListener;
import org.springframework.boot.context.event.ApplicationReadyEvent;

@SpringBootApplication
public class SpringEmail {
    @Autowired
    private EmailSenderService senderService;

    public static void main(String[] args) {
        SpringApplication.run(SpringEmailDemoApplication.class, args)
    }
    @EventListener(ApplicationReadyEvent.class)
    public void sendMail(){
        sederService.sendEmail(toEmail:"", subject: "The subject", body: "The body")
    }
}