import json
import os
import requests
from typing import List, Dict, Any, Optional
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

mcp = FastMCP("insurance")

# Configuration for insurance API - set via environment variable
INSURANCE_API_URL = os.getenv("INSURANCE_API_URL", "")
API_KEY = "img"

def upload_pdf_to_insurance(file_path: str) -> Dict[str, Any]:
    """
    Upload a PDF file to the insurance API for processing
    """
    # Check if API URL is configured
    if not INSURANCE_API_URL:
        return {"error": "INSURANCE_API_URL not configured. Please set it in .env file", "Success": "False"}
    
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}", "Success": "False"}
        
        # Check if file is a PDF
        if not file_path.lower().endswith('.pdf'):
            return {"error": "File must be a PDF", "Success": "False"}
        
        # Prepare the file for upload
        with open(file_path, 'rb') as pdf_file:
            files = {
                API_KEY: (os.path.basename(file_path), pdf_file, 'application/pdf')
            }
            
            # Make POST request to the API
            response = requests.post(INSURANCE_API_URL, files=files)
            response.raise_for_status()
            
            return response.json()
    
    except requests.exceptions.RequestException as e:
        return {
            "error": str(e), 
            "status_code": getattr(e.response, 'status_code', None),
            "Success": "False"
        }
    except Exception as e:
        return {"error": str(e), "Success": "False"}

@mcp.tool()
def process_insurance_certificate(file_path: str) -> Dict[str, Any]:
    """
    Process an insurance certificate PDF file using insurance API
    
    Args:
        file_path: Absolute path to the PDF file to process
    
    Returns:
        JSON response containing extracted insurance certificate data including:
        - CertificateHolder information
        - Classification
        - Coverages (with limits, policy info, endorsements)
        - Insured details
        - Producer information
        - Description of operation
        - Success status
    """
    result = upload_pdf_to_insurance(file_path)
    return result

@mcp.tool()
def get_certificate_holder_info(file_path: str) -> Dict[str, Any]:
    """
    Extract certificate holder information from an insurance certificate PDF
    
    Args:
        file_path: Absolute path to the PDF file to process
    
    Returns:
        Certificate holder information (name, address, city, state, zip code)
    """
    result = upload_pdf_to_insurance(file_path)
    if result.get("Success") == "True":
        return result.get("CertificateHolder", {})
    else:
        return {"error": result.get("error", "Failed to process PDF")}

@mcp.tool()
def get_coverage_details(file_path: str) -> List[Dict[str, Any]]:
    """
    Extract coverage details from an insurance certificate PDF
    
    Args:
        file_path: Absolute path to the PDF file to process
    
    Returns:
        List of coverage details including limits, policy info, and endorsements
    """
    result = upload_pdf_to_insurance(file_path)
    if result.get("Success") == "True":
        return result.get("Coverages", [])
    else:
        return [{"error": result.get("error", "Failed to process PDF")}]

@mcp.tool()
def get_insured_information(file_path: str) -> Dict[str, Any]:
    """
    Extract insured party information from an insurance certificate PDF
    
    Args:
        file_path: Absolute path to the PDF file to process
    
    Returns:
        Insured party information (name, address, city, state, zip code, phone)
    """
    result = upload_pdf_to_insurance(file_path)
    if result.get("Success") == "True":
        return result.get("Insured", {})
    else:
        return {"error": result.get("error", "Failed to process PDF")}

@mcp.tool()
def get_producer_information(file_path: str) -> Dict[str, Any]:
    """
    Extract producer/agent information from an insurance certificate PDF
    
    Args:
        file_path: Absolute path to the PDF file to process
    
    Returns:
        Producer information (name, address, phone, email, fax)
    """
    result = upload_pdf_to_insurance(file_path)
    if result.get("Success") == "True":
        return result.get("Producer", {})
    else:
        return {"error": result.get("error", "Failed to process PDF")}

@mcp.tool()
def validate_certificate_signature(file_path: str) -> Dict[str, Any]:
    """
    Check if the insurance certificate is signed
    
    Args:
        file_path: Absolute path to the PDF file to process
    
    Returns:
        Information about certificate signature status
    """
    result = upload_pdf_to_insurance(file_path)
    if result.get("Success") == "True":
        return {
            "signed": result.get("Signed", "No"),
            "filename": result.get("FileName", []),
            "classification": result.get("Classification", "")
        }
    else:
        return {"error": result.get("error", "Failed to process PDF")}

if __name__ == "__main__":
    mcp.run(transport='stdio') 