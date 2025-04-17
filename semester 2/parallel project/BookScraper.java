import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class BookScraper {
    private static final String BASE_URL = "https://books.toscrape.com/catalogue/";
    private static final String OUTPUT_FILE = "/Users/shehabsalah/Desktop/books.csv"; 
    private static final int NUM_THREADS = 5;

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(NUM_THREADS);
        List<String> data = new ArrayList<>();

        int page = 1;
        while (true) {
            String url = BASE_URL + "page-" + page + ".html";
            if (!pageExists(url)) break;

            ScraperTask task = new ScraperTask(url, data);
            executor.execute(task);
            page++;
        }

        executor.shutdown();
        while (!executor.isTerminated()) {
            // انتظر انتهاء جميع الـ Threads
        }

        saveDataToFile(data);
        System.out.println("✅ Data saved successfully.");
    }

    static boolean pageExists(String url) {
        try {
            Document doc = Jsoup.connect(url).get();
            return doc.select(".product_pod").size() > 0;
        } catch (IOException e) {
            return false;
        }
    }

    static class ScraperTask implements Runnable {
        private final String url;
        private final List<String> data;

        public ScraperTask(String url, List<String> data) {
            this.url = url;
            this.data = data;
        }

        @Override
        public void run() {
            try {
                System.out.println("Scraping: " + url);
                Document doc = Jsoup.connect(url).get();
                Elements books = doc.select(".product_pod");

                synchronized (data) {
                    for (Element book : books) {
                        String title = book.select("h3 a").attr("title");
                        String price = book.select(".price_color").text();
                        String rating = book.select(".star-rating").attr("class").replace("star-rating", "").trim();

                        data.add(title + "," + price + "," + rating);
                        System.out.println("Scraped: " + title);
                    }
                }
            } catch (IOException e) {
                System.out.println("❌ Failed to scrape: " + url);
            }
        }
    }

    static void saveDataToFile(List<String> data) {
        try (FileWriter writer = new FileWriter(OUTPUT_FILE)) {
            writer.write("Title,Price,Rating\n");
            for (String entry : data) {
                writer.write(entry + "\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
