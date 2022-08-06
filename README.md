# Tori

Your Open-source Twitter management tool

## Installation

via clone 

`git clone https://github.com/Eliran-Turgeman/Tori.git`

## Usage

Create a txt file with the contents of your thread.
Every paragraph will be treated as a separate tweet.

Example:

Given the file `thread.txt` with the following content

```
Experimenting with Twitter API!

Now it's a thread

I'll tell you all about it later...
```

Execute

`python3 main.py thread.txt`

Will result in the following [thread](https://twitter.com/_eltur/status/1555823529836306432) 


Note that in order to execute this tool, you will need to define your consumer key and consumer key secret as environment variables

```
export TWITTER_CONSUMER_KEY="..."
export TWITTER_CONSUMER_SECRET="..."
```

To get the above keys, go to Twitter [developer portal](https://developer.twitter.com/en/portal/dashboard) and create a new application.
