# The Counted

[The Counted](http://www.theguardian.com/us-news/ng-interactive/2015/jun/01/the-counted-police-killings-us-database) is a database made available by [The Gaurdian](http://www.theguardian.com) to document police killings in the United States.

This repo is just to grab the data as a csv file and do a little exploration with python scripts.

The source data can be found at the following link: http://interactive.guim.co.uk/2015/the-counted/thecounted-data.zip

Also available is an [RDF Data Cube](https://dvcs.w3.org/hg/gld/raw-file/default/data-cube/index.html) at: https://cdn.rawgit.com/nicholsn/the-counted/master/the-counted-2016.ttl

### Data Updates
- Updated csv on 2015-06-23 21:32:58.618100
- Updated csv on 2016-06-26 16:48:14.532935
- Updated csv on 2016-06-26 16:48:56.259132

<script type="application/ld+json">
{
  "@context":"https://schema.org/",
  "@type":"Dataset",
  "name":"The Counted",
  "description":"The Counted is a database made available by The Gaurdian to document police killings in the United States.",
  "url":"http://www.nolan-nichols.com/the-counted",
  "sameAs":"https://data.world/nicholsn/2016-police-killings-us-db",
  "keywords":[
     "POLICE"
  ],
  "creator":{
     "@type":"Person",
     "url": "https://orcid.org/0000-0003-1099-3328",
     "name":"Nolan Nichols"
  },
  "distribution":[
     {
        "@type":"DataDownload",
        "encodingFormat":"CSV",
        "contentUrl":"https://raw.githubusercontent.com/nicholsn/the-counted/master/the-counted-2016.csv"
     },
     {
        "@type":"DataDownload",
        "encodingFormat":"TTL",
        "contentUrl":"https://raw.githubusercontent.com/nicholsn/the-counted/master/the-counted-2016.ttl"
     }
  ],
  "temporalCoverage":"2016-01-01/2016-12-31"
  }
}
</script>
