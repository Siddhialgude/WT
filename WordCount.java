import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.SparkSession;
import scala.Tuple2;
import java.util.Arrays;
  
public class WordCount {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("WordCount")
                .master("local[*]")
                .getOrCreate(); 

        JavaSparkContext jsc = new JavaSparkContext(spark.sparkContext());

        JavaRDD<String> lines = jsc.textFile("input.txt");
        JavaRDD<String> words = lines.flatMap(line -> Arrays.asList(line.split(" ")).iterator());

        JavaPairRDD<String, Integer> wordCounts = words.mapToPair(word -> new Tuple2<>(word, 1));

        JavaPairRDD<String, Integer> counts = wordCounts.reduceByKey((x, y) -> x + y);

        counts.foreach(pair -> System.out.println(pair._1 + ": " + pair._2));

        spark.stop();
        jsc.stop();
    }
}

#javac -cp "/usr/local/spark-3.5.1-bin-hadoop3/jars/*" -source 8 -target 8 WordCount.java
#jar cvf WordCount.jar WordCount.class
#spark-submit --class WordCount --master local[*] WordCount.jar input.txt