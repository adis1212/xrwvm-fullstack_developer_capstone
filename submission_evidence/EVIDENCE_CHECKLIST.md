# IBM Full Stack Application Development Capstone — Evidence Checklist

**Student / GitHub:** adis1212  
**Repository:** [xrwvm-fullstack_developer_capstone](https://github.com/adis1212/xrwvm-fullstack_developer_capstone)  
**Branch:** main  

---

## Complete Question-by-Question Status Table

| Coursera Question | Task Description | Required File / Format | Generated | Verified | Ready to Submit | File Location |
|:---|:---|:---|:---:|:---:|:---:|:---|
| **Q1** | Fork and clone repo, update README | `README.md` | Yes | Yes | Yes | `README.md` |
| **Q2** | Static pages branch / setup | Git commit/branch | Yes | Yes | Yes | In Git history |
| **Q3** | About Us static page | `About.html` | Yes | Yes | Yes | `server/frontend/static/About.html` |
| **Q4** | Contact Us static page | `Contact.html` | Yes | Yes | Yes | `server/frontend/static/Contact.html` |
| **Q5** | Django User Login API | `loginuser` | Yes | Yes | Yes | `submission_evidence/terminal_outputs/loginuser` |
| **Q6** | Django User Logout API | `logoutuser` | Yes | Yes | Yes | `submission_evidence/terminal_outputs/logoutuser` |
| **Q7** | React User Registration component | `Register.jsx` | Yes | Yes | Yes | `server/frontend/src/components/Register/Register.jsx` |
| **Q8** | Dealer Reviews proxy API | `getdealerreviews` | Yes | Yes | Yes | `submission_evidence/terminal_outputs/getdealerreviews` |
| **Q9** | Get All Dealerships proxy API | `getalldealers` | Yes | Yes | Yes | `submission_evidence/terminal_outputs/getalldealers` |
| **Q10** | Get Dealer Details by ID (dealer 8) | `getdealerbyid` | Yes | Yes | Yes | `submission_evidence/terminal_outputs/getdealerbyid` |
| **Q11** | Get Dealers by State (Kansas) | `getdealersbyState` | Yes | Yes | Yes | `submission_evidence/terminal_outputs/getdealersbyState` |
| **Q12** | Django Admin authenticated page (root) | `admin_login.png` | Yes | Yes | Yes | `submission_evidence/screenshots/admin_login.png` |
| **Q13** | Django Admin logged-out page | `admin_logout.png` | Yes | Yes | Yes | `submission_evidence/screenshots/admin_logout.png` |
| **Q14** | Car makes and models API | `getallcarmakes` | Yes | Yes | Yes | `submission_evidence/terminal_outputs/getallcarmakes` |
| **Q15** | Review Sentiment Analyzer ("Fantastic services") | `analyzereview` | Yes | Yes | Yes | `submission_evidence/terminal_outputs/analyzereview` |
| **Q16** | Dealers page before login (logged out) | `get_dealers.png` | Yes | Yes | Yes | `submission_evidence/screenshots/get_dealers.png` |
| **Q17** | Dealers page after login (with Review option) | `get_dealers_loggedin.png` | Yes | Yes | Yes | `submission_evidence/screenshots/get_dealers_loggedin.png` |
| **Q18** | Dealers filtered by state (Kansas) | `dealersbystate.png` | Yes | Yes | Yes | `submission_evidence/screenshots/dealersbystate.png` |
| **Q19** | Dealer details and customer reviews page | `dealer_id_reviews.png` | Yes | Yes | Yes | `submission_evidence/screenshots/dealer_id_reviews.png` |
| **Q20** | Post Review form filled before submission | `dealership_review_submission.png` | Yes | Yes | Yes | `submission_evidence/screenshots/dealership_review_submission.png` |
| **Q21** | Newly posted review visible on dealer page | `added_review.png` | Yes | Yes | Yes | `submission_evidence/screenshots/added_review.png` |
| **Q22** | GitHub Actions CI/CD workflow run output | `CI/CD` | Yes | Yes | Yes | `submission_evidence/terminal_outputs/CI/CD` |
| **Q23** | Public deployment URL | `deploymentURL` | Yes | Yes | Yes | `submission_evidence/terminal_outputs/deploymentURL` |
| **Q24** | Deployed landing page screenshot | `deployed_landingpage.png` | Yes | Yes | Yes | `submission_evidence/screenshots/deployed_landingpage.png` |
| **Q25** | Deployed logged-in page screenshot | `deployed_loggedin.png` | Yes | Yes | Yes | `submission_evidence/screenshots/deployed_loggedin.png` |
| **Q26** | Deployed dealer details page screenshot | `deployed_dealer_detail.png` | Yes | Yes | Yes | `submission_evidence/screenshots/deployed_dealer_detail.png` |
| **Q27** | Deployed posted review screenshot | `deployed_add_review.png` | Yes | Yes | Yes | `submission_evidence/screenshots/deployed_add_review.png` |

---

## Deployment Details

- **Deployment URL:** `https://patent-statement-countries-angel.trycloudflare.com`
- **Method:** Cloudflare Quick Tunnel → Django dev server on port 8000
- **Tunnel verified at:** 2026-11-12T22:30:53+05:30

---

## Exact Terminal Outputs Content (Verified)

### Q5: `loginuser`
```json
{"userName": "testuser", "status": "Authenticated"}
```

### Q6: `logoutuser`
```json
{"userName": ""}
```

### Q8: `getdealerreviews`
```json
{"status": 200, "reviews": [{"_id": "6af5e914ac7e797117e08984", "id": 1, "name": "Berkly Shepley", "dealership": 15, "review": "Total grid-enabled service-desk", "purchase": true, "purchase_date": "07/11/2020", "car_make": "Audi", "car_model": "A6", "car_year": 2010, "__v": 0, "sentiment": "neutral"}, {"_id": "6af5e914ac7e797117e089a8", "id": 37, "name": "Albrecht Collen", "dealership": 15, "review": "Pre-emptive heuristic solution", "purchase": true, "purchase_date": "10/10/2020", "car_make": "Lexus", "car_model": "IS F", "car_year": 2009, "__v": 0, "sentiment": "neutral"}, {"_id": "6af5e914ac7e797117e089a9", "id": 38, "name": "Prudi Minchi", "dealership": 15, "review": "Mandatory homogeneous groupware", "purchase": true, "purchase_date": "01/06/2021", "car_make": "Saturn", "car_model": "L-Series", "car_year": 2001, "__v": 0, "sentiment": "neutral"}]}
```

### Q9: `getalldealers`
Returns array of all 50 dealership objects with status 200 (length 12,502 bytes).

### Q10: `getdealerbyid`
```json
{"status": 200, "dealer": [{"_id": "6af5e914ac7e797117e089be", "id": 8, "city": "Topeka", "state": "Kansas", "address": "288 Larry Place", "zip": "66642", "lat": "39.0429", "long": "-95.7697", "short_name": "Bytecard", "full_name": "Bytecard Car Dealership", "__v": 0}]}
```

### Q11: `getdealersbyState`
```json
{"status": 200, "dealers": [{"_id": "6af5e914ac7e797117e089be", "id": 8, "city": "Topeka", "state": "Kansas", "address": "288 Larry Place", "zip": "66642", "lat": "39.0429", "long": "-95.7697", "short_name": "Bytecard", "full_name": "Bytecard Car Dealership", "__v": 0}]}
```

### Q14: `getallcarmakes`
```json
{"CarModels": [{"CarModel": "Pathfinder", "CarMake": "NISSAN"}, {"CarModel": "Qashqai", "CarMake": "NISSAN"}, {"CarModel": "XTRAIL", "CarMake": "NISSAN"}, {"CarModel": "A-Class", "CarMake": "Mercedes"}, {"CarModel": "C-Class", "CarMake": "Mercedes"}, {"CarModel": "E-Class", "CarMake": "Mercedes"}, {"CarModel": "A4", "CarMake": "Audi"}, {"CarModel": "A5", "CarMake": "Audi"}, {"CarModel": "A6", "CarMake": "Audi"}, {"CarModel": "Sorrento", "CarMake": "Kia"}, {"CarModel": "Carnival", "CarMake": "Kia"}, {"CarModel": "Cerato", "CarMake": "Kia"}, {"CarModel": "Corolla", "CarMake": "Toyota"}, {"CarModel": "Camry", "CarMake": "Toyota"}, {"CarModel": "Kluger", "CarMake": "Toyota"}]}
```

### Q15: `analyzereview`
```json
{"sentiment": "positive"}
```

### Q23: `deploymentURL`
```
https://patent-statement-countries-angel.trycloudflare.com
```
