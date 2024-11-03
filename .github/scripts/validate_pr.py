import os
import sys
from github import Github
from github import GithubException

def validate_env_vars():
    """Validate required environment variables."""
    required_vars = ['GITHUB_TOKEN', 'PR_NUMBER', 'REPO_NAME', 'AUTHOR']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Error: Missing required environment variables: {', '.join(missing_vars)}")
        sys.exit(1)

def calculate_score(g, repo_name, author, pr_number):
    """Calculate contribution score based on various metrics."""
    try:
        # Initialize GitHub repository
        repo = g.get_repo(repo_name)
        scores = {}
        
        print(f"Evaluating contributions for {author} in {repo_name}")
        
        # Get all PRs by the user
        all_prs = list(repo.get_pulls(state='all'))
        user_prs = [pr for pr in all_prs if pr.user.login == author]
        
        # PR Volume Score (15%)
        pr_volume = len(user_prs)
        scores['pr_volume'] = min((pr_volume / 10) * 15, 15)
        print(f"PR Volume: {pr_volume} PRs, Score: {scores['pr_volume']:.2f}%")
        
        # Merged PRs Score (15%)
        merged_prs = [pr for pr in user_prs if pr.merged]
        scores['merged_prs'] = (len(merged_prs) / max(pr_volume, 1)) * 15
        print(f"Merged PRs: {len(merged_prs)} PRs, Score: {scores['merged_prs']:.2f}%")
        
        # Issues Score (10%)
        user_issues = list(repo.get_issues(creator=author))
        scores['issues'] = min((len(user_issues) / 5) * 10, 10)
        print(f"Issues: {len(user_issues)} issues, Score: {scores['issues']:.2f}%")
        
        # Comments Score (15%)
        issue_comments = list(repo.get_issues_comments())
        user_comments = [comment for comment in issue_comments if comment.user.login == author]
        scores['comments'] = min((len(user_comments) / 20) * 15, 15)
        print(f"Comments: {len(user_comments)} comments, Score: {scores['comments']:.2f}%")
        
        # Documentation Score (5%)
        doc_prs = [pr for pr in user_prs if 'doc' in pr.title.lower() or 'readme' in pr.title.lower()]
        scores['docs'] = min((len(doc_prs) / 3) * 5, 5)
        print(f"Documentation: {len(doc_prs)} contributions, Score: {scores['docs']:.2f}%")
        
        # Calculate total score
        total_score = sum(scores.values())
        print(f"Total Score: {total_score:.2f}%")
        
        return total_score, scores
        
    except GithubException as e:
        print(f"GitHub API Error: {str(e)}")
        print(f"Status: {e.status}")
        print(f"Data: {e.data}")
        raise
    except Exception as e:
        print(f"Error calculating scores: {str(e)}")
        raise

def create_review_message(total_score, scores):
    """Create formatted review message with scores."""
    message = "# PR Evaluation Results\n\n"
    message += f"Total Score: {total_score:.2f}%\n\n"
    message += "## Breakdown:\n"
    message += f"- PR Volume: {scores['pr_volume']:.2f}% / 15%\n"
    message += f"- Merged PRs: {scores['merged_prs']:.2f}% / 15%\n"
    message += f"- Issues: {scores['issues']:.2f}% / 10%\n"
    message += f"- Comments: {scores['comments']:.2f}% / 15%\n"
    message += f"- Documentation: {scores['docs']:.2f}% / 5%\n\n"
    
    PASSING_SCORE = 60
    
    if total_score >= PASSING_SCORE:
        message += "✅ Congratulations! Your contributions meet our criteria."
    else:
        message += f"❌ Your contributions don't meet our minimum criteria of {PASSING_SCORE}%.\n\n"
        message += "### Suggestions for improvement:\n"
        message += "- Submit more quality PRs\n"
        message += "- Engage more in discussions and code reviews\n"
        message += "- Contribute to documentation\n"
        message += "- Help resolve issues\n"
    
    return message

def main():
    """Main function to evaluate PR and create review."""
    try:
        print("Validating environment variables...")
        validate_env_vars()
        
        # Get environment variables
        token = os.getenv('GITHUB_TOKEN')
        repo_name = os.getenv('REPO_NAME')
        pr_number = int(os.getenv('PR_NUMBER'))
        author = os.getenv('AUTHOR')
        
        print(f"Starting evaluation for PR #{pr_number} by {author}")
        print(f"Repository: {repo_name}")
        
        # Initialize GitHub client
        g = Github(token)
        print("GitHub client initialized")
        
        repo = g.get_repo(repo_name)
        print("Repository accessed successfully")
        
        pr = repo.get_pull(pr_number)
        print("Pull request accessed successfully")
        
        # Calculate scores
        total_score, scores = calculate_score(g, repo_name, author, pr_number)
        
        # Create review message
        review_message = create_review_message(total_score, scores)
        print("Review message created")
        
        # Create PR review
        PASSING_SCORE = 60
        review_event = 'APPROVE' if total_score >= PASSING_SCORE else 'REQUEST_CHANGES'
        
        pr.create_review(
            body=review_message,
            event=review_event
        )
        
        print(f"PR review created with status: {review_event}")
        
    except Exception as e:
        print(f"Error in main function: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
