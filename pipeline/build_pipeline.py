from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
import os
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()
logger = get_logger(__name__)
def main():
    try:
        logger.info("Starting Anime Recommender Pipeline")
        
        # Load anime data
        loader = AnimeDataLoader("/Users/elifsakin/Desktop/anime recommender/data/anime_with_synopsis.csv"
                                 ,"/Users/elifsakin/Desktop/anime recommender/data/anime_updated.csv")
        processed_csv = loader.load_and_process()
        logger.info(f"Data loaded and processed successfully: {processed_csv}")
        # Build and save vector store
        vector_builder = VectorStoreBuilder(
            csv_path=processed_csv)
        vector_builder.build_and_save_vector_store()
        logger.info("Vector store built and saved successfully")
    except Exception as e:
        logger.error(f"Error in main pipeline: {e}")
        raise CustomException(f"Pipeline execution failed: {e}")
if __name__ == "__main__":
    main()