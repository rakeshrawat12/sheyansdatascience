# Portfolio Website

A professional MERN stack portfolio website for Rakesh Singh Rawat - Data Scientist.

## Structure

```
portfolio/
├── client/          # React frontend (Vite)
├── server/          # Express backend
```

## Getting Started

### 1. Install Dependencies

```bash
# Install server dependencies
cd server
npm install

# Install client dependencies
cd ../client
npm install
```

### 2. Set Up MongoDB

- Create a MongoDB Atlas account or use local MongoDB
- Copy `server/.env.example` to `server/.env`
- Update `MONGO_URI` with your connection string

### 3. Run the Application

```bash
# Terminal 1 - Start backend
cd server
npm run dev

# Terminal 2 - Start frontend
cd client
npm run dev
```

### 4. Open in Browser

Visit `http://localhost:3000`

## Features

- Dark theme modern design
- Responsive layout for all devices
- Hero section with animated text
- About page with statistics
- Projects showcase with tech tags
- Skills section with visual progress bars
- Contact form with MongoDB storage
- Smooth page navigation
