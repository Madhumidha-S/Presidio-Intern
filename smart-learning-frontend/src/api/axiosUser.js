import axios from "axios";
import Cookies from "js-cookie";

const userApi = axios.create({
  baseURL: "http://localhost:3000/user",
  withCredentials: true,
});

export default userApi;
