import pandas as pd
import re
from difflib import SequenceMatcher

def clean_title(s):
    """
    Clean proposal title by removing emoticons, quotes, and standardizing spaces
    """
    s = str(s)
    s = re.sub(r'[\U0001F300-\U0001F9FF]', '', s)
    s = s.replace('"', '').replace("'", "").strip()
    return ' '.join(s.split())

def title_similarity(a, b):
    """
    Calculate similarity ratio between two strings
    """
    return SequenceMatcher(None, a, b).ratio()

def analyze_proposal_matches(voting_file, proposals_file, similarity_threshold=0.95):
    """
    Analyze proposal matches with tolerance for minor differences
    """
    # Load only the Proposal columns
    voting_df = pd.read_csv(voting_file, usecols=['Proposal'])
    proposals_df = pd.read_csv(proposals_file, usecols=['Proposal'])
    
    print(f"Loaded {len(voting_df)} voting records and {len(proposals_df)} proposals")
    
    # Clean all titles
    voting_titles = [clean_title(title) for title in voting_df['Proposal']]
    proposal_titles = [clean_title(title) for title in proposals_df['Proposal']]
    
    # First try exact matches
    voting_set = set(voting_titles)
    exact_matches = []
    near_matches = []
    unmatched = []
    
    # For each proposal, try exact match first, then similarity if needed
    for prop in proposal_titles:
        if prop in voting_set:
            exact_matches.append(prop)
        else:
            # Try to find a close match
            best_ratio = 0
            best_match = None
            for vote_title in voting_titles:
                ratio = title_similarity(prop, vote_title)
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_match = vote_title
            
            if best_ratio >= similarity_threshold:
                near_matches.append((prop, best_match, best_ratio))
            else:
                unmatched.append(prop)
    
    # Prepare summary
    summary = {
        'Total Proposals': len(proposal_titles),
        'Total Voting Records': len(voting_titles),
        'Exact Matches': len(exact_matches),
        'Near Matches': len(near_matches),
        'Total Matches': len(exact_matches) + len(near_matches),
        'Unmatched Proposals': len(unmatched),
        'Match Rate': f"{((len(exact_matches) + len(near_matches)) / len(proposal_titles) * 100):.2f}%"
    }
    
    # Print summary
    print("\nMatch Analysis Summary:")
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    # Show near matches
    if near_matches:
        print("\nNear Matches Found (sample up to 5):")
        for prop, vote, ratio in near_matches[:5]:
            print(f"\nProposal: {prop}")
            print(f"Matched with: {vote}")
            print(f"Similarity: {ratio:.3f}")
    
    # Show unmatched
    if unmatched:
        print("\nUnmatched Proposals (sample up to 5):")
        for prop in unmatched[:5]:
            print(f"- {prop}")
    
    return exact_matches, near_matches, unmatched

if __name__ == "__main__":
    voting_file = "Fund11_voting_data.csv"
    proposals_file = "Fund11 Proposals.csv"
    
    exact_matches, near_matches, unmatched = analyze_proposal_matches(voting_file, proposals_file)
