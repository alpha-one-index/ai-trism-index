# AWS Data Exchange Setup Guide — ai-trism-index

This guide covers setting up the automated S3 upload and AWS Data Exchange (ADX) pipeline for hourly AI TRiSM vendor market data.

## Overview

The `update-data.yml` workflow now includes steps to:
1. Upload `vendors.json` and `fetch-report.json` to S3 every hour
2. Create a new ADX revision with the latest TRiSM market data
3. Auto-finalize the revision so subscribers get updates automatically

The AWS steps are **gated by secrets** — they only run when `ADX_DATASET_ID` is configured.

## Step 1: Create S3 Bucket

```bash
aws s3 mb s3://ai-trism-index-data --region us-east-1
aws s3api put-bucket-versioning \
  --bucket ai-trism-index-data \
  --versioning-configuration Status=Enabled
```

## Step 2: Create IAM User

Minimal permissions policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject", "s3:ListBucket"],
      "Resource": ["arn:aws:s3:::ai-trism-index-data", "arn:aws:s3:::ai-trism-index-data/*"]
    },
    {
      "Effect": "Allow",
      "Action": ["dataexchange:CreateRevision", "dataexchange:CreateJob", "dataexchange:StartJob", "dataexchange:GetJob", "dataexchange:UpdateRevision"],
      "Resource": "*"
    }
  ]
}
```

## Step 3: Create ADX Dataset

1. Go to [AWS Data Exchange Console](https://console.aws.amazon.com/dataexchange/)
2. Create data set:
   - **Name**: AI TRiSM Vendor Market Intelligence Index
   - **Description**: Hourly-updated AI Trust, Risk, and Security Management vendor data. Tracks vendor website status, acquisition signals, and regulatory compliance across the TRiSM ecosystem.
3. Note the **Dataset ID**

## Step 4: Add GitHub Secrets

Repo Settings > Secrets > Actions:

| Secret | Value |
|---|---|
| `AWS_ACCESS_KEY_ID` | IAM user access key |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key |
| `ADX_DATASET_ID` | Dataset ID from Step 3 |

## S3 Structure

```
s3://ai-trism-index-data/
  trism-market-data/
    latest/
      vendors.json
      fetch-report.json
    snapshots/
      2026-03-08T06:00-vendors.json
      2026-03-08T07:00-vendors.json
      ...
```

## Data Highlights for Subscribers

- Hourly vendor website health monitoring
- Acquisition signal detection (M&A activity tracking)
- Regulatory source verification
- Vendor count and category breakdowns

## Cost Estimate

- S3: ~$0.03/month (hourly snapshots, small JSON)
- ADX provider: Free
- GitHub Actions: ~720 runs/month (within free tier for public repos)
