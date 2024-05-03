import java.io.IOException;
//Imports the Path class from the org.apache.hadoop.fs package. This class represents a file or directory path in the Hadoop distributed filesystem (HDFS). 
import org.apache.hadoop.fs.Path;
//Imports the ConfiguraƟon class from the org.apache.hadoop.conf package. This class manages Hadoop configuraƟon seƫngs.
import org.apache.hadoop.conf.Configuration;
//Imports various input/output classes from the org.apache.hadoop.io package. These classes are used for data serializaƟon and deserializaƟon in Hadoop.
import org.apache.hadoop.io.*;
// Imports classes and interfaces for the MapReduce framework from the org.apache.hadoop.mapreduce package. 
import org.apache.hadoop.mapreduce.*;
//Imports the FileInputFormat class from the org.apache.hadoop.mapreduce.lib.input package. It provides funcƟonality for specifying the input format for MapReduce jobs.
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
//Imports the FileOutputFormat class from the org.apache.hadoop.mapreduce.lib.output package. It provides funcƟonality for specifying the output format for MapReduce jobs.
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
  
public class WeatherAverage {
	public static class WeatherMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
//Declares an instance variable outputKey of type Text. It is used to store the output key for the mapper. 
		private Text outputKey = new Text();
//Declares an instance variable outputValue of type IntWritable. It is used to store the output value for the mapper. 
		private IntWritable outputValue = new IntWritable();

		public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
//Context: Context context: Context object to interact with the Hadoop framework (e.g., emiƫng output key-value pairs). 
			String[] tokens = value.toString().split("\\s+"); // Spliƫng by whitespace
			if (tokens.length >= 4) {
				// ExtracƟng dateƟme, temperature, dew point, and wind speed
				String datetime = tokens[0] + " " + tokens[1];
				double temperature = Double.parseDouble(tokens[2]);
				double dewPoint = Double.parseDouble(tokens[3]);
				int windSpeed = Integer.parseInt(tokens[4]);
				// Emiƫng temperature
				outputKey.set("Temperature");
				outputValue.set((int) temperature);
				context.write(outputKey, outputValue);
				// Emiƫng dew point
				outputKey.set("Dew Point");
				outputValue.set((int) dewPoint);
				context.write(outputKey, outputValue);
				// Emiƫng wind speed
				outputKey.set("Wind Speed");
				outputValue.set(windSpeed);
				context.write(outputKey, outputValue);
			}
		}
	}

	public static class WeatherReducer extends Reducer<Text, IntWritable, Text, DoubleWritable> {
		private DoubleWritable result = new DoubleWritable();

		public void reduce(Text key, Iterable<IntWritable> values, Context context)
				throws IOException, InterruptedException {
//Iterable<IntWritable> represents a collecƟon of IntWritable values associated with the key, allowing the reducer to iterate over them and perform computaƟons.
			int sum = 0;
			int count = 0;
			for (IntWritable val : values) { // values: collecƟon of values
				sum += val.get();
				count++;
			}
			double average = (double) sum / count;
			result.set(average);
			context.write(key, result);
		}
	}

	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
//"job" refers to the unit of work that you want to execute on a Hadoop cluster. 
//This line sets the JAR file containing the Java classes for the MapReduce job 
		Job job = Job.getInstance(conf, "Weather Average");
// It specifies the class responsible for mapping input key-value pairs to intermediate keyvalue pairs. 
		job.setJarByClass(WeatherAverage.class);
//It specifies the class responsible for reducing intermediate key-value pairs to final output key-value pairs. 
		job.setMapperClass(WeatherMapper.class);
		job.setReducerClass(WeatherReducer.class);
		job.setOutputKeyClass(Text.class);          
		job.setOutputValueClass(IntWritable.class);
		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
//This line submits the MapReduce job for execuƟon and waits for it to complete. It returns 0 if the job completes successfully or 1 if there is an error. 
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}


/*
 * start-dfs
 * start-yarn
 * jps
 * hadoop fs -mkdir /input12
 * hadoop fs -put C:/sample_weather.txt /input12
 * hadoop fs -ls /input12/
 * hadoop jar C:/Jarfile/weather.jar /input12 /weatheroutput
 * hadoop fs -cat /weatheroutput/*
 */
*/