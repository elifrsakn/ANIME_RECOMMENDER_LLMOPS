from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)
class AnimeRecommendationPipeline:
    def __init__(self, persist_dir: str = "chroma_db"):
        try: 
            logger.info("Initializing AnimeRecommendationPipeline")
            vector_builder = VectorStoreBuilder(
                csv_path="",
                persist_dir=persist_dir
            )
            retriever = vector_builder.load_vector_store().as_retriever()
            logger.info("Vector store loaded successfully")
            self.recommender = AnimeRecommender(retriever, GROQ_API_KEY, MODEL_NAME)
            logger.info("AnimeRecommender initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing AnimeRecommendationPipeline: {e}")
            raise CustomException(f"Failed to initialize pipeline: {e}")

    def recommend(self, query: str):  # <-- buraya dikkat
        try:
            logger.info(f"Getting recommendation for query: {query}")
            recommendation = self.recommender.get_recommendation(query)
            logger.info("Recommendation retrieved successfully")
            return recommendation
        except Exception as e:
            logger.error(f"Error getting recommendation: {e}")
            raise CustomException(f"Failed to get recommendation: {e}")
