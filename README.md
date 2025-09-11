# AGROKASA - Advertisement Management Platform

A modern web-based advertisement management platform for agricultural products built with NiceGUI.

## Features

### Frontend (Current Implementation)
- ✅ **Homepage**: Displays all adverts in a responsive grid layout
- ✅ **Add Advert Form**: Complete form with Title, Description, Price, Category, Quantity, and Image upload
- ✅ **Edit Advert**: Pre-populated form for updating existing adverts
- ✅ **View Advert**: Detailed view of individual advertisements
- ✅ **Responsive Design**: Mobile-first design that works on all devices
- ✅ **Navigation**: Clean header with navigation links
- ✅ **User Feedback**: Success/error notifications for user actions

### Backend Integration Ready
- 🔄 **API Service Layer**: Prepared for backend integration
- 🔄 **Data Models**: Structured for easy backend connection

## Project Structure

```
advertisement_manager/
├── assets/                 # Static images and media files
├── components/
│   └── header.py          # Navigation header component
├── pages/
│   ├── home.py           # Homepage with advert grid
│   ├── add_advert.py     # Add new advert form
│   ├── edit_advert.py    # Edit existing advert form
│   └── view_advert.py    # View advert details
├── main.py               # Application entry point
└── requirements.txt      # Python dependencies
```

## Installation & Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python main.py
   ```

3. **Access the Application**
   - Open your browser and navigate to `http://localhost:8080`

## Backend Integration

The frontend is ready for backend integration. Your colleague should implement the following API endpoints:

### Required API Endpoints

1. **GET /api/adverts** - Get all advertisements
2. **GET /api/adverts/{id}** - Get specific advert details  
3. **POST /api/adverts** - Create new advertisement
4. **PUT /api/adverts/{id}** - Update existing advertisement
5. **DELETE /api/adverts/{id}** - Delete advertisement

### Backend Integration

The frontend is ready for direct backend integration. Sample data is currently hardcoded in each page for development purposes.

## Form Fields

### Add/Edit Advert Form
- **Title** (required): Product name
- **Description** (required): Detailed product description
- **Price** (required): Price in GHC
- **Category** (required): Product category from predefined list
- **Quantity**: Amount available (e.g., "10 kg")
- **Image**: Product photo upload

### Categories Available
- Fruits
- Vegetables  
- Grains & Legumes
- Herbs & Spices
- Dairy & Eggs
- Meat & Poultry
- Nuts
- Tubers
- Seedlings

## Responsive Design

The platform is fully responsive with:
- **Mobile**: 1 column grid
- **Tablet**: 2-3 column grid  
- **Desktop**: 3-4 column grid
- **Large screens**: 4+ column grid

## Technologies Used

- **NiceGUI**: Python web framework
- **Tailwind CSS**: Utility-first CSS framework
- **Google Fonts**: Poppins, Roboto, Lobster fonts

## Next Steps for Backend Integration

1. Replace hardcoded sample data with actual API calls
2. Add error handling for API failures
3. Implement user authentication if needed
4. Add image upload handling to backend
5. Connect form submissions to backend endpoints
