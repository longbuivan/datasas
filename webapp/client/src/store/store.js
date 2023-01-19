// eslint-disable-next-line import/no-extraneous-dependencies
import { applyMiddleware, combineReducers, compose, createStore } from "redux";
import thunk from "redux-thunk";
import { reducer as reduxFormReducer } from "redux-form";
import PostsReducer from "./reducers/PostsReducer";
import { AuthReducer } from "./reducers/AuthReducer";
// import rootReducers from './reducers/Index';
import todoReducers from "./reducers/Reducers";

const middleware = applyMiddleware(thunk);

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const reducers = combineReducers({
  posts: PostsReducer,
  auth: AuthReducer,
  todoReducers,
  form: reduxFormReducer,
});

// const store = createStore(rootReducers);

export const store = createStore(reducers, composeEnhancers(middleware));
export default {};
