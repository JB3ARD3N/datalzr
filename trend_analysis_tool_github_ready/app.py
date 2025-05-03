from ingestion.reddit_ingest import fetch_reddit_data
from ingestion.twitter_ingest import fetch_twitter_data
from ingestion.file_ingest import load_from_file
from storage.database import init_db, store_data
from dashboard.dashboard import run_dashboard

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default='dashboard', help='dashboard | ingest_reddit | ingest_twitter | ingest_file')
    parser.add_argument('--file', type=str, help='Path to test file')
    parser.add_argument('--keywords', nargs='+', default=["trending products", "new business ideas", "pain points"])
    args = parser.parse_args()

    init_db()

    if args.mode == 'ingest_reddit':
        data = fetch_reddit_data(args.keywords)
        store_data(data)
    elif args.mode == 'ingest_twitter':
        data = fetch_twitter_data(args.keywords)
        store_data(data)
    elif args.mode == 'ingest_file' and args.file:
        data = load_from_file(args.file)
        store_data(data)
    else:
        run_dashboard()
