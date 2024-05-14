import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  try {
    const picturePromise = uploadPhoto(); const picture = await picturePromise;
    const userPromise = createUser(); const user = await userPromise;
    console.log(`${picture.body} ${user.firstName} ${user.lastName}`);
  } catch (error) {
    console.log('Signup system offline');
  }
}
