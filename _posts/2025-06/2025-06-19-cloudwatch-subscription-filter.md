---
title: "CloudWatch Subscription Filter"
published: true
tags: AWS
---

A **CloudWatch Logs subscription filter** allows you to **stream log data in real time** from CloudWatch Logs to other services like:

- **Amazon Kinesis Data Streams**
- **Amazon Kinesis Data Firehose**
- **AWS Lambda**
- **Amazon OpenSearch Service (via Firehose)**

### ✅ Use Cases

- Real-time processing (e.g., alerting or anomaly detection)
- Indexing logs in OpenSearch
- Storing logs in S3 via Firehose
- Streaming logs to Lambda for custom logic

---

### 🔧 How It Works

1. **Log Group**: The source of the logs (e.g., `/aws/lambda/my-function`).
2. **Destination**: The target (Lambda, Firehose, etc.).
3. **Filter Pattern** (optional): A pattern to extract or match specific log entries.

---

### 📘 Example: Send logs to Lambda

```bash
aws logs put-subscription-filter \
  --log-group-name "/aws/lambda/my-function" \
  --filter-name "MySubscription" \
  --filter-pattern "" \
  --destination-arn "arn:aws:lambda:region:account-id:function:my-function" \
  --role-arn "arn:aws:iam::account-id:role/CloudWatchLogsToLambdaRole"
```

- `filter-pattern ""` means forward **all logs**.
- The role must grant `logs:PutSubscriptionFilter` and invoke permissions on the Lambda.

---

### 📝 Notes

- Only **one subscription filter per log group** is allowed.
- You can use [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html) for querying, but it's separate from subscription filters.
- Delivery is **near real-time**, usually within a few seconds.
