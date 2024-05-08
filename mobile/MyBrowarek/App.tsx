import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import Constants from 'expo-constants'

function App() {
  return (
    <View className="flex-1 items-center justify-center">
      <Text>Open up App.tsx to start working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

let entryPoint = App;
if (Constants.expoConfig?.extra && Constants.expoConfig.extra.storybookEnabled === 'true') {
  entryPoint = require('./.storybook').default;
}

export default entryPoint;