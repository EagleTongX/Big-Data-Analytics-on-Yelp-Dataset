# Big-Data-Analytics-on-Yelp-Dataset

**Directories explanation**
  /data_ingest
    code for ingest dataset to hdfs
  /etl_code
    code for creating tables and basic query
  /profiling_code
    code for cleaning and exploring the property of each table
  /analytics
    all the code developed for this project

**Usage**
1. Dataset for downloading: https://www.yelp.com/dataset
  For this project, we use five datasets in total, eg business.json, checkin.json, photo.json, review.json and user.json
2. Ingest the dataset to HDFS
  Code for ingesting is in folder /data_ingest. Please execute them using shell.
3. Build the table
  The schema and code for creating tables are in folder /etl_code. Please execute them using hive-shell
4. Analytics
  Code for data analytics is in sourcecode_for_analytics.txt. Please execute them using hive-shell.
  You can find results in the output section.

**Explanation**

Calculate photo score
  select count(*) from photo2;
    280992
  select count(distinct business_id) from photo2;
    32976
  normalization
  select business_id, count(*)/280992*32976 as normCount from photo2 group by business_id order by normCount;
  CREATE VIEW IF NOT EXISTS photoRanking AS select business_id, count(*)/280992*32976 as normCount from photo2 group by business_id order by normCount;

Calculate checkin score
  select sum(checkin2.count) from checkin2;
    17915884
  select count(distinct business_id) from checkin2;
    157075
  CREATE VIEW IF NOT EXISTS checkinRanking AS select business_id, sum(checkin2.count)/17915884*157075 as normCount from checkin2 group by business_id order by normCount;

Calculate review score
  CREATE VIEW IF NOT EXISTS reviewRanking AS select sum(review.stars*(0.6*review.useful+0.4*user.compliment)/user.review_count) as score, review.business_id from user, review where review.user_id=user.user_id group by review.business_id;

Build ranking system
  create table finalRanking as select photoranking.business_id, 0.5*photoranking.normcount+0.2*checkinRanking.normcount+0.3*reviewRanking.score as finalnorm from photoRanking, checkinRanking, reviewRanking where photoranking.business_id=checkinRanking.business_id and photoranking.business_id=reviewRanking.business_id;

Evaluation:
Extract 10% from the checkin data and compare the total ranking with our system and yelp's system
  yelp's ranking
    select sum(businesswithcountId.id) from checkinwithId, businesswithcountId
    where checkinwithId.id%10=0 and businesswithcountId.review_count>10 and checkinwithId.business_id= businesswithcountId.business_id;
  our ranking
    select sum(finalRankingwithId.id) from checkinwithId, finalRankingwithId where checkinwithId.id%10=0 and checkinwithId.business_id= finalRankingwithId.business_id;
    

