import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class NewsService {

    private final String apiKey = "NEWS_API_KEY"; 
    private final String apiUrl = "https://newsapi.org/v2/everything";

    public String fetchEconomicNews() {
        RestTemplate restTemplate = new RestTemplate();

        String url = apiUrl + "?q=economy&sortBy=publishedAt&apiKey=" + apiKey;
        NewsApiResponse response = restTemplate.getForObject(url, NewsApiResponse.class);

        if (response != null && response.getArticles() != null) {
            return response.getArticles().stream()
                    .map(article -> String.format("Title: %s\nURL: %s\n", article.getTitle(), article.getUrl()))
                    .collect(Collectors.joining("\n\n"));
        }
        return "No economic news available at the moment.";
    }
}
