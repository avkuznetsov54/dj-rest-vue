import store from "@/store";
import { getAPI } from "@/api/mortgages/axios-mortgages";

const mortgagesModule = {
  namespaced: true,
  state: {
    MORTGAGES_DATA: null
  },
  getters: {},
  mutations: {
    SET_UPDATE_MORTGAGES_DATA(state, data) {
      state.MORTGAGES_DATA = data;
    },
    destroy_MORTGAGES_DATA(state) {
      state.MORTGAGES_DATA = null;
    }
  },
  actions: {
    FETCH_MORTGAGES(context, params) {
      // console.log(url);
      return new Promise((resolve, reject) => {
        getAPI
          .get("api/v1/mortgages/all/", {
            headers: {
              Authorization: `Bearer ${store.state.accessToken}`
            },
            params: params
          }) // proof that your access token is still valid; if not the
          // axios getAPI response interceptor will attempt to get a new  access token from the server. check out ../api/axios-base.js getAPI instance response interceptor
          .then(response => {
            // console.log("GetAPI successfully got the mods");
            // console.log(response);
            context.commit("SET_UPDATE_MORTGAGES_DATA", response.data.results); // store the response data in store
            resolve(response);
          })
          .catch(err => {
            // refresh token expired or some other error status
            // eslint-disable-next-line no-unused-vars
            const er = err; // просто чтоб ошибку в консоли не показывало
            // console.log(err);
            console.log("[mortgages] Не получилось");
            reject(err);
          });
      });
    }
  }
};

export default mortgagesModule;
