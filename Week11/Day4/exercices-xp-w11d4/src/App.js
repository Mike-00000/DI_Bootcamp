import React from "react";
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import ErrorBoundary from "./ErrorBoundary";
import HomeScreen from "./HomeScreen";
import ProfileScreen from "./ProfileScreen";
import ShopScreen from "./ShopScreen";
import PostList from "./PostList";
import Example1 from "./Example1";
import Example2 from "./Example2";
import Example3 from "./Example3";

const App = () => {
  return (
    <BrowserRouter>
      <div>
        <nav className="navbar navbar-expand navbar-dark bg-dark">
          <div className="container">
            <ul className="navbar-nav">
              <li className="nav-item">
                <NavLink exact to="/" className="nav-link">
                  Home
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/profile" className="nav-link">
                  Profile
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/shop" className="nav-link">
                  Shop
                </NavLink>
              </li>
            </ul>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<ErrorBoundary><HomeScreen /></ErrorBoundary>} />
          <Route path="/profile" element={<ErrorBoundary><ProfileScreen /></ErrorBoundary>} />
          <Route path="/shop" element={<ErrorBoundary><ShopScreen /></ErrorBoundary>} />
          <Route path="/postlist" element={<ErrorBoundary><PostList /></ErrorBoundary>} />
        </Routes>

        <div>
          <h1>Hi This is a Title</h1>
          <PostList />
        </div>
      </div>

      <div>
        <Example1 />
        <Example2 />
        <Example3 />
      </div>
    </BrowserRouter>
  );
};

export default App;
