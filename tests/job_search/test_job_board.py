"""
Job board interface module for the Research and Preparation agent.
Provides abstract and concrete implementations for different job boards.
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union
from dataclasses import dataclass
from datetime import datetime


@dataclass
class JobPosting:
    """Data class to represent a job posting."""
    id: str
    title: str
    company: str
    location: str
    description: str
    url: str
    date_posted: datetime
    salary_info: Optional[str] = None
    job_type: Optional[str] = None  # full-time, part-time, contract, etc.
    requirements: Optional[List[str]] = None
    is_remote: bool = False
    raw_data: Optional[Dict] = None  # Store the original raw data for reference


class JobBoardInterface(ABC):
    """Abstract base class for job board interfaces."""
    
    @abstractmethod
    def search(self, 
               keywords: List[str], 
               location: Optional[str] = None,
               radius: Optional[int] = None,
               job_type: Optional[List[str]] = None,
               remote: bool = False,
               experience_level: Optional[List[str]] = None,
               posted_within_days: Optional[int] = None,
               limit: int = 50) -> List[JobPosting]:
        """
        Search for jobs with the given parameters.
        
        Args:
            keywords: List of job title or skill keywords
            location: Job location (city, state, country)
            radius: Search radius in miles/km from the location
            job_type: List of job types (full-time, part-time, contract, etc.)
            remote: Whether to search for remote jobs only
            experience_level: List of experience levels (entry, mid, senior)
            posted_within_days: Only include jobs posted within this many days
            limit: Maximum number of results to return
            
        Returns:
            List of JobPosting objects matching the search criteria
        """
        pass
    
    @abstractmethod
    def get_job_details(self, job_id: str) -> JobPosting:
        """
        Get detailed information about a specific job.
        
        Args:
            job_id: The unique identifier for the job
            
        Returns:
            A JobPosting object with detailed information
        """
        pass
    
    @abstractmethod
    def is_rate_limited(self) -> bool:
        """
        Check if we're currently being rate limited by the job board.
        
        Returns:
            True if rate limited, False otherwise
        """
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Name of the job board."""
        pass


class LinkedInJobBoard(JobBoardInterface):
    """Implementation of JobBoardInterface for LinkedIn."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the LinkedIn job board interface.
        
        Args:
            api_key: Optional API key for LinkedIn API access
        """
        self._api_key = api_key
        self._rate_limited = False
        self._last_request_time = None
        self._min_request_interval = 1.0  # seconds between requests
    
    @property
    def name(self) -> str:
        return "LinkedIn"
    
    def search(self,
               keywords: List[str],
               location: Optional[str] = None,
               radius: Optional[int] = None,
               job_type: Optional[List[str]] = None,
               remote: bool = False,
               experience_level: Optional[List[str]] = None,
               posted_within_days: Optional[int] = None,
               limit: int = 50) -> List[JobPosting]:
        """
        Search for jobs on LinkedIn with the given parameters.
        
        For now, this uses a mock implementation. The actual implementation
        would use the LinkedIn API or web scraping.
        """
        # In a real implementation, this would make an API call or scrape the website
        # For now, we'll return a mock result for testing purposes
        mock_results = []
        
        # Create some mock job postings for testing
        # In a real implementation, these would be created from API/scraped data
        mock_job = JobPosting(
            id="linkedin-job-123",
            title="Senior Software Engineer",
            company="Tech Company Inc.",
            location="San Francisco, CA",
            description="We're looking for a senior software engineer...",
            url="https://linkedin.com/jobs/view/123",
            date_posted=datetime.now(),
            salary_info="$120,000 - $150,000",
            job_type="full-time",
            requirements=["Python", "AWS", "5+ years experience"],
            is_remote=True,
            raw_data={"original_data": "would be here"}
        )
        mock_results.append(mock_job)
        
        return mock_results[:limit]
    
    def get_job_details(self, job_id: str) -> JobPosting:
        """Get detailed information about a specific LinkedIn job."""
        # In a real implementation, this would make an API call or scrape the job page
        # For now, return a mock job posting
        return JobPosting(
            id=job_id,
            title="Senior Software Engineer",
            company="Tech Company Inc.",
            location="San Francisco, CA",
            description="Detailed job description with requirements...",
            url=f"https://linkedin.com/jobs/view/{job_id}",
            date_posted=datetime.now(),
            salary_info="$120,000 - $150,000",
            job_type="full-time",
            requirements=["Python", "AWS", "5+ years experience"],
            is_remote=True,
            raw_data={"original_data": "would be here"}
        )
    
    def is_rate_limited(self) -> bool:
        """Check if we're currently being rate limited by LinkedIn."""
        return self._rate_limited


class IndeedJobBoard(JobBoardInterface):
    """Implementation of JobBoardInterface for Indeed."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Indeed job board interface.
        
        Args:
            api_key: Optional API key for Indeed API access
        """
        self._api_key = api_key
        self._rate_limited = False
        self._last_request_time = None
        self._min_request_interval = 1.5  # seconds between requests
    
    @property
    def name(self) -> str:
        return "Indeed"
    
    def search(self,
               keywords: List[str],
               location: Optional[str] = None,
               radius: Optional[int] = None,
               job_type: Optional[List[str]] = None,
               remote: bool = False,
               experience_level: Optional[List[str]] = None,
               posted_within_days: Optional[int] = None,
               limit: int = 50) -> List[JobPosting]:
        """
        Search for jobs on Indeed with the given parameters.
        
        For now, this uses a mock implementation. The actual implementation
        would use the Indeed API or web scraping.
        """
        # Mock implementation for testing
        mock_results = []
        
        mock_job = JobPosting(
            id="indeed-job-456",
            title="Python Developer",
            company="Software Solutions LLC",
            location="New York, NY",
            description="Looking for a Python developer with web experience...",
            url="https://indeed.com/jobs/view/456",
            date_posted=datetime.now(),
            salary_info="$90,000 - $110,000",
            job_type="full-time",
            requirements=["Python", "Django", "3+ years experience"],
            is_remote=False,
            raw_data={"original_data": "would be here"}
        )
        mock_results.append(mock_job)
        
        return mock_results[:limit]
    
    def get_job_details(self, job_id: str) -> JobPosting:
        """Get detailed information about a specific Indeed job."""
        # Mock implementation for testing
        return JobPosting(
            id=job_id,
            title="Python Developer",
            company="Software Solutions LLC",
            location="New York, NY",
            description="Detailed job description for Python developer role...",
            url=f"https://indeed.com/jobs/view/{job_id}",
            date_posted=datetime.now(),
            salary_info="$90,000 - $110,000",
            job_type="full-time",
            requirements=["Python", "Django", "3+ years experience"],
            is_remote=False,
            raw_data={"original_data": "would be here"}
        )
    
    def is_rate_limited(self) -> bool:
        """Check if we're currently being rate limited by Indeed."""
        return self._rate_limited


class GlassdoorJobBoard(JobBoardInterface):
    """Implementation of JobBoardInterface for Glassdoor."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Glassdoor job board interface.
        
        Args:
            api_key: Optional API key for Glassdoor API access
        """
        self._api_key = api_key
        self._rate_limited = False
        self._last_request_time = None
        self._min_request_interval = 2.0  # seconds between requests
    
    @property
    def name(self) -> str:
        return "Glassdoor"
    
    def search(self,
               keywords: List[str],
               location: Optional[str] = None,
               radius: Optional[int] = None,
               job_type: Optional[List[str]] = None,
               remote: bool = False,
               experience_level: Optional[List[str]] = None,
               posted_within_days: Optional[int] = None,
               limit: int = 50) -> List[JobPosting]:
        """
        Search for jobs on Glassdoor with the given parameters.
        
        For now, this uses a mock implementation. The actual implementation
        would use the Glassdoor API or web scraping.
        """
        # Mock implementation for testing
        mock_results = []
        
        mock_job = JobPosting(
            id="glassdoor-job-789",
            title="Frontend Developer",
            company="WebUI Technologies",
            location="Austin, TX",
            description="Seeking a skilled frontend developer...",
            url="https://glassdoor.com/jobs/view/789",
            date_posted=datetime.now(),
            salary_info="$85,000 - $105,000",
            job_type="full-time",
            requirements=["JavaScript", "React", "2+ years experience"],
            is_remote=True,
            raw_data={"original_data": "would be here"}
        )
        mock_results.append(mock_job)
        
        return mock_results[:limit]
    
    def get_job_details(self, job_id: str) -> JobPosting:
        """Get detailed information about a specific Glassdoor job."""
        # Mock implementation for testing
        return JobPosting(
            id=job_id,
            title="Frontend Developer",
            company="WebUI Technologies",
            location="Austin, TX",
            description="Detailed job description for frontend developer role...",
            url=f"https://glassdoor.com/jobs/view/{job_id}",
            date_posted=datetime.now(),
            salary_info="$85,000 - $105,000",
            job_type="full-time",
            requirements=["JavaScript", "React", "2+ years experience"],
            is_remote=True,
            raw_data={"original_data": "would be here"}
        )
    
    def is_rate_limited(self) -> bool:
        """Check if we're currently being rate limited by Glassdoor."""
        return self._rate_limited


class JobBoardFactory:
    """Factory class to create job board instances."""
    
    @staticmethod
    def create(board_name: str, api_key: Optional[str] = None) -> JobBoardInterface:
        """
        Create a job board instance by name.
        
        Args:
            board_name: Name of the job board ("linkedin", "indeed", "glassdoor")
            api_key: Optional API key for the job board
            
        Returns:
            A JobBoardInterface implementation
            
        Raises:
            ValueError: If the board name is not recognized
        """
        board_name = board_name.lower()
        
        if board_name == "linkedin":
            return LinkedInJobBoard(api_key)
        elif board_name == "indeed":
            return IndeedJobBoard(api_key)
        elif board_name == "glassdoor":
            return GlassdoorJobBoard(api_key)
        else:
            raise ValueError(f"Unknown job board: {board_name}")